# Overview
With this challenge, we are greeted with a fun little game that generates a random number every time you click the button.

# Analysis
After seeing the source code, we see that the button sends a POST request with two values: generate and score.

# Attack Execution
We can use CURL to send a POST request with a score over 999999 (If you send a POST request with just a score parameter, it won’t work, make sure to include the generate value as well). We can use the CURL command:
curl --request POST --form 'generate=Give+a+try%21' --form 'score=1000000' http://challenge01.root-me.org/web-serveur/ch56/
