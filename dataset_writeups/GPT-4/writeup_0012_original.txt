Title: Local File Inclusion Exploit to Access Sensitive Files

During a CTF event, I encountered a web application that allowed users to view various pages through a URL parameter. The application would dynamically load the content of a specified file into the web page. This functionality raised the suspicion of a potential Local File Inclusion (LFI) vulnerability, which could be exploited to access sensitive files on the server.

To test for an LFI vulnerability, I crafted a URL that included a relative file path to a sensitive file on the server, such as /etc/passwd. For example, if the original URL was https://example.com/view?page=about.html, I modified it to https://example.com/view?page=../../../../etc/passwd.

Upon navigating to the modified URL, the application returned a web page that displayed the contents of the /etc/passwd file, confirming the presence of an LFI vulnerability.

By further exploiting the LFI vulnerability and accessing other sensitive files on the server, I was able to locate the flag required for the Web Exploitation challenge.

This CTF writeup highlights the importance of properly validating and sanitizing user-supplied file paths in web applications to prevent LFI vulnerabilities. By exploiting the LFI vulnerability, I was able to access sensitive server files and obtain the flag needed to complete the challenge.
