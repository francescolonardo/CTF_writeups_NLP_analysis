Title: Exploiting Insecure Direct Object References to Access Unauthorized Files

During a CTF competition, I came across a web application that utilized numeric IDs in the URL to reference specific files. This caught my attention, as it could potentially be vulnerable to Insecure Direct Object Reference (IDOR) attacks, allowing unauthorized access to restricted files.

To test for an IDOR vulnerability, I logged in to the application with a regular user account and navigated to a file accessible to that user. The URL looked like this: https://example.com/files/123. I then tried incrementing and decrementing the numeric ID in the URL to see if I could access files that were not intended for my user account.

By modifying the numeric ID, I was able to access files that belonged to other users, including a file containing the flag for the Web Exploitation challenge.

This CTF writeup emphasizes the importance of implementing proper access controls and authorization mechanisms in web applications to prevent IDOR vulnerabilities. By exploiting the IDOR vulnerability, I was able to gain unauthorized access to restricted files and find the flag needed to complete the challenge.
