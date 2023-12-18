Title: Empire3

# Overview
We are presented the usual company website, we register and login as usual and we try to add a todo {{config}}.

# Analysis
We go in the list of todos and we have a lot of information, the most important is the flask secret key which is used to sign the cookies.
Now we check if there is any cookie saved by the website and we find that there is one. Decrypting it with flask-session-cookie-manager we discover that it contains a user_id field, maybe we can change it and login as another user.

# Attack Execution
We try set user_id to 1 and we encode the cookie again. As we send the cookie we actually login as jarret.booz but no flag here. LetaTMs try user_id = 2 and we actually find the flag.