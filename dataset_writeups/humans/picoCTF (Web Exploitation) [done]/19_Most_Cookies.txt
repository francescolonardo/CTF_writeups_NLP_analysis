Title: Most Cookies

Let's visit the site. And analyze the source code.
The `/display` page checks the session cookie. 
From this, it is clear we need to become admin to swipe that flag!
We need to change the `very_auth` session value to `admin` somehow.
Looking at the server script (`server.py`) code, we can see that the Flask session secret key is hardcoded into the source code! This key is set to a random cookie name.
This secret key is used to sign a flask session cookie so that it cannot be modified. However, since we know the secret key is one of the 28 cookie names, we can simply try them all until we successfully decrypt the cookie.
We use a Python script to bruteforce each secret in the wordlist.
So, the first step is to go to the website and copy a valid session cookie.
Use our old friend Developer Tools: `Inspect > Application > Storage > Cookies`.
Let's use CyberChef to decode that cookie value (it was base64 encoded).
We observe that the header is `{ "very_auth": "blank" }`
Yikes. We want to be `admin` instead of `blank`.
With the secret key, we can craft our own session cookie.
Putting this new crafted cookie back into Burp Suite, we get the flag in the response.
