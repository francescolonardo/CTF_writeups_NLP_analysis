Title: Cookie Tampering to Gain Unauthorized Access

In a recent CTF competition, I encountered a web application that utilized cookies to store user authentication and authorization information. This caught my attention, as it could potentially be vulnerable to cookie tampering attacks, allowing unauthorized access to restricted areas of the application.

To investigate this possibility, I logged in to the application with a regular user account and inspected the cookies stored in my browser. I noticed a cookie named "user_role" with the value "user". I suspected that the application might be using this cookie to determine the user's access level.

To test the vulnerability, I edited the "user_role" cookie's value and changed it from "user" to "admin". After modifying the cookie, I refreshed the web page to see if the application would grant me administrative privileges.

To my surprise, the application recognized me as an admin user and granted me access to the restricted admin panel. Inside the admin panel, I found the flag for the Web Exploitation challenge.

This CTF writeup highlights the importance of implementing proper security measures for handling user authentication and authorization, especially when using cookies. By tampering with the cookie, I was able to gain unauthorized access to the admin panel and find the flag needed to complete the challenge.
