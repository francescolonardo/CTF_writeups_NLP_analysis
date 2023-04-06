Title: Post Practice

This is actually a very easy challenge if you know about HTTP, I don't know why the author gave it a Medium difficulty. Let's begin.

From the description alone we understand what is the challenge about. Make a POST request, and pass login information, the question is how it should look like and what information we need to pass.

In the page we don't see much, checking the source will give us the credentials for the login.

Nicely commented us `username: admin | password: 71urlkufpsdnlkadsf` so now we know what are the parameters we need to send, and what are their values. Let's do that.

For this task, you are required to play around with the HTTP-request header. By using Burp Suite, the request is originally a GET.

Our objective is to change the request from GET to POST. If you look at the response, you should find the username and password for the POST request.

As I said the challenge is very easy, it's not even a hard thing to learn how POST request works and what is it. But checking the comments I saw a mention of curl which is a tool for sending request using URLs, and that might be a faster way to solve it (not that requests is bad, but knowing more tools is good).
