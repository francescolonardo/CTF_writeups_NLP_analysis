Title: Local File Inclusion Exploit to Access Sensitive Files

During a CTF competition, I came across a web application that allowed users to view different pages using a URL parameter, such as http://example.com/page?file=about. The URL structure caught my attention, as the application might be vulnerable to Local File Inclusion (LFI), potentially allowing access to sensitive files on the server.

To test for an LFI vulnerability, I attempted to include a local file from the server by modifying the file parameter in the URL, such as http://example.com/page?file=../../../../etc/passwd. If the web application displayed the contents of the /etc/passwd file, it would confirm the presence of an LFI vulnerability.

Upon submitting the modified URL, the web application indeed displayed the contents of the /etc/passwd file, confirming the LFI vulnerability. To exploit the vulnerability and obtain the flag for the Web Exploitation challenge, I tried to access other sensitive files on the server, such as configuration files or log files that might contain valuable information.

After exploring various files, I found a sensitive file that contained the flag for the Web Exploitation challenge. By exploiting the LFI vulnerability, I was able to access sensitive files on the server and obtain the flag needed to complete the challenge.

This CTF writeup highlights the importance of properly validating and sanitizing user input in web applications to prevent LFI vulnerabilities. By exploiting the LFI vulnerability, I gained access to sensitive files on the server and obtained the flag needed to complete the challenge.
