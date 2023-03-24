Title: Exploiting Insecure Direct Object References to Access Sensitive Data

During a CTF competition, I encountered a web application that allowed users to view their own profile information. Upon inspecting the URL structure, I noticed that the user profile IDs were included in the URL as plain integers, such as http://example.com/profile?id=123. This caught my attention, as the application might be vulnerable to Insecure Direct Object References (IDOR), potentially allowing unauthorized access to other users' profiles and sensitive data.

To test for an IDOR vulnerability, I modified the user profile ID in the URL to a different integer value, such as http://example.com/profile?id=124. If the web application displayed another user's profile information without proper access control, it would confirm the presence of an IDOR vulnerability.

By incrementing the user profile IDs and exploring different profiles, I discovered a user with a higher level of privileges, such as an administrator. Within the administrator's profile, I found sensitive information that included the flag for the Web Exploitation challenge.

This CTF writeup highlights the importance of implementing proper access control mechanisms and securing direct object references in web applications to prevent unauthorized access to sensitive data. By exploiting the IDOR vulnerability, I was able to access other users' profiles, including an administrator's profile, and obtain the flag needed to complete the challenge.
