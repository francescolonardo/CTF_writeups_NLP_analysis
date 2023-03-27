Title: Cookie Tampering to Elevate Privileges and Access Restricted Area

During a CTF competition, I encountered a web application that used cookies to store user session information. Upon inspecting the cookies, I noticed a cookie named user_role with a value of user. This caught my attention, as it suggested that the application might be storing privilege levels in cookies, potentially allowing privilege escalation through cookie tampering.

To test for a possible vulnerability, I decided to modify the value of the user_role cookie from user to admin using a browser extension or a proxy tool like Burp Suite. If the web application granted access to an admin panel or a restricted area after modifying the cookie value, it would confirm a vulnerability in the privilege management system.

After changing the user_role cookie value to admin and refreshing the page, the web application indeed granted access to an admin panel, confirming the vulnerability. Inside the admin panel, I discovered a page containing the flag for the Web Exploitation challenge.

This CTF writeup emphasizes the importance of implementing secure session management and storing sensitive information server-side rather than relying on client-side cookies. By tampering with the user_role cookie, I was able to elevate my privileges, gain unauthorized access to the admin panel, and obtain the flag needed to complete the challenge.
