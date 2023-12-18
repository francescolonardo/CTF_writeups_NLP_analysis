Title: Power Cookie

As suggested by the challenge name, the solution likely involves changing a cookie value.
If we go to the website, we find that there are no cookies saved. However, if we click the `continue as guest` button, we can see, using the Developer Tools that a cookie with the name `admin` is generated, with the value 0.
0 means `False` here, so if we change the cookie's value to 1 (`True`) and refresh, the website treats us like the admin, giving us the flag.