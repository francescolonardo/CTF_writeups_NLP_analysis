Title: Exploiting LFI to Retrieve Sensitive Configuration Files

During a CTF event, I found a web application that allowed users to view specific files on the server through a URL parameter. This caught my attention, as it could potentially be vulnerable to a Local File Inclusion (LFI) attack, enabling an attacker to access sensitive files on the server.

To test for an LFI vulnerability, I tried to manipulate the URL parameter to view system files that shouldn't be accessible to a regular user. For example, I attempted to access the /etc/passwd file by modifying the URL to https://example.com/view_file?file=../../../../etc/passwd.

Upon navigating to the modified URL, the web application displayed the content of the /etc/passwd file, confirming the presence of an LFI vulnerability.

To exploit this vulnerability, I focused on retrieving sensitive configuration files from the server, which might contain important information such as database credentials or the flag for the Web Exploitation challenge. By manipulating the URL parameter, I accessed various configuration files and eventually found a file containing the flag.

This CTF writeup highlights the importance of implementing secure methods for handling user input in web applications to prevent LFI vulnerabilities. By exploiting the LFI vulnerability, I was able to access sensitive configuration files and obtain the flag needed to complete the challenge.
