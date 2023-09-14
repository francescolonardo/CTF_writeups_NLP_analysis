## Angular of the Universe 
The challenge was about bypassing the Angular application that was set up behind Nginx reverse proxy. The challenge contained two flags:
- first was hidden in the angular endpoint `/debug/answer` restricted by the Nginx and the application
- second hidden in the express endpoint `/api/true-answer` which yielded results only for `127.0.0.1` IP addresses.

### Flag#2 /api/true-answer (149 points, 34 solves) 
As mentioned, the application was displaying the flag if the request came from the loopback network.

```js

  server.get('/api/true-answer', (req, res) => {
    console.log('HIT: %s', req.ip)
    if (req.ip.match(/127\.0\.0\.1/)) {
      res.json(`hello admin, this is true answer: ${process.env.FLAG2}`)
    } else {
      res.status(500).send('Access restricted!')
    }
  });

```

Because the application was hidden behind Nginx proxy, `req.ip` was always pointing to the same IP address of the reverse proxy. The application didn't also trust `X-Forwarded-*` headers so this value couldn't be overridden. 

When accessing `/q` endpoint, the application was displaying contents of `/api/answer`. It was done on the server-side via the below snippet.

```ts
  ngOnInit(): void {
    ...
    // fetch answer via API
    this.service.getAnswer().subscribe((answer: string) => {
      this.answer = answer
    })
  }
}
```

`this.service.getAnswer()` was yielding `this.http.get('/api/answer')`.


```ts
  getAnswer() {
    return this.http.get('/api/answer')
  }
```

Apparently angular when doing HTTP requests uses `Host` header, something around `PROTOCOL + HOST + / PATH`. Not only that but also follows the redirects. Therefore by providing a custom host and redirecting anything to `127.0.0.1/api/true-answer`, we get the flag. 

```sh
curl 'http://universe.chal.ctf.westerns.tokyo/a' -H 'Host: terjanq.me'
```

#### TWCTF{you-have-to-eat-tomato-yume-chan!}
