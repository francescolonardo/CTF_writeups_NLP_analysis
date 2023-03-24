Title: Directory Traversal Attack to Access Sensitive Files

In a recent CTF event, I came across a web application that allowed users to view files hosted on the server by providing a file path as part of the URL. This functionality led me to suspect that the application might be vulnerable to a Directory Traversal attack, allowing unauthorized access to sensitive files outside the intended directory.

To test for a Directory Traversal vulnerability, I crafted a URL that included a relative file path to a sensitive file on the server, such as /etc/passwd. For example, if the original URL was https://example.com/view?file=example.txt, I modified it to https://example.com/view?file=../../../../etc/passwd.

Upon navigating to the modified URL, the application returned a web page that displayed the contents of the /etc/passwd file, confirming the presence of a Directory Traversal vulnerability.

By further exploiting the Directory Traversal vulnerability and accessing other sensitive files on the server, I was able to locate the flag required for the Web Exploitation challenge.

This CTF writeup emphasizes the importance of properly validating and sanitizing user-supplied file paths in web applications to prevent Directory Traversal vulnerabilities. By exploiting the Directory Traversal vulnerability, I was able to access sensitive server files and obtain the flag needed to complete the challenge.
