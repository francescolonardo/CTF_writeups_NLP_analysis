Title: Cookie Manipulation to Gain Administrative Privileges

During a CTF event, I came across a web application that utilized cookies to store user session information. This caught my attention, as manipulating cookies can sometimes lead to privilege escalation or unauthorized access to restricted resources.

To test for cookie manipulation vulnerabilities, I logged in to the application with a regular user account and examined the cookies using my browser's developer tools. I noticed that there was a cookie named "role" with a value of "user". This led me to suspect that the application might be using this cookie to determine the user's privileges.

I decided to manipulate the "role" cookie to see if I could gain administrative privileges. I changed the cookie value from "user" to "admin" and refreshed the web page. Upon doing so, I gained access to an administrative panel that was previously hidden.

Inside the administrative panel, I found the flag for the Web Exploitation challenge.

This CTF writeup highlights the importance of implementing secure methods for handling user sessions and privileges in web applications, such as server-side session management. By manipulating the "role" cookie, I was able to escalate my privileges and gain unauthorized access to the administrative panel, where I found the flag needed to complete the challenge.
