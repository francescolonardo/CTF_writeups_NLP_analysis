# Overview
When visiting the web page for this challenge, we are asked for credentials.

# Analysis
However, the intended solution for this challenge is not to manipulate input sanitization, but to tamper with different HTTP methods, called verb tampering.

# Attack Execution
We can use curl commands to request the web page with different verbs, and find the password. We can use this curl command to get the password (other verbs also yield the same result).
curl --request PUT http://challenge01.root-me.org/web-serveur/ch8/
