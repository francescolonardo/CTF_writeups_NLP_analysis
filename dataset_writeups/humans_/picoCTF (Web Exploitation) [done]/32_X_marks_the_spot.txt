Title: X marks the spot

Visiting the website, we are presented with a login form (and a Robert Frost poem).

The hint says "XPATH", and using some common XPATH injection techniques we can leak some information about the underlying DB.

The idea is similar to SQL injection. We have a vulnerable query for authenticating the username and password.
So, if we inject some valid XPATH vocabulary into the query, we can manipulate it.

Experimenting with the query we can check if the password of the first username is longer than 1 character. If we submit this as the username, we get back a response from the server telling us that "You're on the right path", so we can deduce that password is longer than 1.
In the same way we can check that the password is shorter than 30 characters.

Let's use the following syntax to iterate some users and check if someone's password starts with "a", "b", "c", etc.

We can write a script that uses XPATH substring to brute force the password character by character.
