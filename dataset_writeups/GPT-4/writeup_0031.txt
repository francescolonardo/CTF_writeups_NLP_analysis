Title: Exploiting Insecure Cookie Handling for Privilege Escalation

During a CTF event, I discovered a web application that used cookies to store and manage user authentication and authorization information. This caught my attention, as improper cookie handling can lead to vulnerabilities that allow attackers to escalate their privileges and access sensitive information.

To test the web application's cookie handling, I logged in with a low-privileged user account and inspected the cookies using browser developer tools. I noticed that the user's role was stored in a cookie named "role," with a value of "user."

To exploit the potential vulnerability, I attempted to modify the "role" cookie value to "admin" using the browser's developer tools or a cookie editing extension. After changing the cookie value, I refreshed the web page and observed that the application granted me administrative privileges, allowing me to access restricted areas of the application.

With administrative access, I navigated to the administrative panel, where I found sensitive information, including the flag for the Web Exploitation challenge. By submitting the flag, I completed the challenge.

This CTF writeup highlights the importance of securely handling cookies in web applications to prevent unauthorized privilege escalation. By exploiting the insecure cookie handling, I was able to escalate my privileges and obtain the flag needed to complete the challenge.
