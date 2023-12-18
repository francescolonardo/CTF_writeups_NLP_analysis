# Overview
We start the challenge with a login portal that says we’re not authenticated and can’t view this page (take note of the URI).

# Analysis
If you change the URI to contain index.php, it will quickly go to that page, and redirect back to the one we started at. You can use burp suite, ZAP proxy, or curl to capture the request. I used the curl command:
curl "http://challenge01.root-me.org/web-serveur/ch32/index.php"

If you want to do the challenge properly, you can use burp suite or any other program that intercepts server responses. When in burp suite, go the proxy tab, and then options tab, and enable Intercept Server Responses (this is off by default).

# Attack Execution
Then, turn on intercept and request the same webpage as we did in the curl command above. Forward the requests until you get a response, it should be an HTTP 302 Found response. Change the code to 200 OK and forward the response to your browser, you should get a web page with the flag.
