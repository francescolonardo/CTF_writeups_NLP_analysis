Title: Don't Bump Your Head(er)

When you visit the site, you can find the clue in the HTML code:
"Sorry, it seems as if your user agent is not correct, in order to access this website."

From the clue above, we have to change the User-Agent to Sup3rS3cr3tAg3nt before we send the request to the site.

Using Postman, change the user agent and send GET request to /header.php. You will get this response:
"Sorry, it seems as if you did not just come from the site, 'awesomesauce.com'."

You have to change the Referer in the header to awesomesauce.com then you send GET request again to /header.php. The response contains the flag in it.
