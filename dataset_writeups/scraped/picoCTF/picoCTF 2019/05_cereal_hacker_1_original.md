Title: cereal hacker 1

It will be foundamental later. After a ton of guessing and a little hint from the official discord page of picoCTF we found that the credentials to log in as a regular user were: username=guest and password=guest.
The really intresting part in this page are the cookies, in fact there is a new cookie base64 encoded called user_info.

Credential bruteforcing: The credentials can be found with hydra and the http[s]-{get|post}-form module.

The user= and pass= are the post variables found from the debugging console in Firefox.

Login as guest:guest.

Get cookie.
URL and Base64Decode using CyberChef.
Change the cookie.
Encoding using CyberChef.
Set cookie to new cookie.
Change URL to file=admin.
You got the flag.