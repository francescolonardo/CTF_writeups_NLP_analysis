Title: Get aHEAD

Looking at the HTML of the website, we can see that both red and blue buttons make a request to the same URL, however with different HTTP request methods. We can make the educated guess that the flag will be acessible by using a different HTTP request method.
Using the tool Burp Suite, we can try HTTP requests with different request methods. Unfortunately, both "PUT" and "DELETE" do not result in the flag.
Looking at the MDN Web Docs, we can see that there are actually 9 different HTTP request methods, one of which being "HEAD". 
As this challenge is named "Get aHEAD", we can conclude that we must use the "HEAD" method to get the flag.