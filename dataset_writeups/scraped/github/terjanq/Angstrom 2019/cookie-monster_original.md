# Cookie Monster
Once again, we've got a simple webpage with URL reporting functionality. After a quick inspection we see two endpoints `/getflag` and `/cookies`. When visiting `/cookies` our `cookies` are being displayed and it looks like `user_DE7aL1xDCe3BauCWqSVqg_0C5bu2078UgQHIqYsF2h0= 311`. That's a valid variable in JavaScript so by including this script on the prepared website 
```
<script src='https://cookiemonster.2019.chall.actf.co/cookies'></script>
```
and then reading the window variable
```javascript
var name = Object.getOwnPropertyNames(window).filter(x=>x.indexOf('admin')!=-1)[0];
```
we get the admin's cookie `admin_GgxUa7MQ7UVo5JHFGLbqzuQfFFy4EDQNwZWAWJXS5_o=` and then the flag: **actf{defund_is_the_real_cookie_monster}**