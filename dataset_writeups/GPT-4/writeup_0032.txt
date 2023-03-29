Title: File Inclusion Vulnerability: Accessing Sensitive Files through LFI

During a CTF competition, I encountered a web application that allowed users to load specific pages by passing a parameter through the URL. This functionality caught my attention, as it might be vulnerable to Local File Inclusion (LFI) attacks, which could potentially allow me to access sensitive files on the server.

To test for an LFI vulnerability, I manipulated the URL parameter to include system files, such as /etc/passwd. For example, if the original URL was http://example.com/?page=about, I modified it to http://example.com/?page=../../../../etc/passwd.

When the web application displayed the content of the /etc/passwd file, it confirmed the presence of an LFI vulnerability.

To exploit the LFI vulnerability and retrieve the flag for the Web Exploitation challenge, I crafted a URL that would include the flag file from the server's file system. For example, I used the following URL: http://example.com/?page=../../../../path/to/flag.txt.

After submitting the crafted URL, the web application included the content of the flag file, allowing me to obtain the flag needed to complete the challenge.

This CTF writeup emphasizes the importance of properly validating and sanitizing user input in web applications to prevent file inclusion vulnerabilities. By exploiting the LFI vulnerability, I was able to access sensitive files on the server and obtain the flag needed to complete the challenge.
