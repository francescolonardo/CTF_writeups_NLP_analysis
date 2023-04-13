Title: Empire2

# Overview
First of all letaTMs register and login, then we try to create a todo with {{config}} and we can see in the list of todos a lot of information about the flask server

# Analysis
We can see the secret key to sign cookies.
Get the flask session cookie encoded.

# Attack Execution
And if we decode it with flask-session-cookie-manager we actually find our flag.
