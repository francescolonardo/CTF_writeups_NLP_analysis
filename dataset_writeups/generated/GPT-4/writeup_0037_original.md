Title: Exploiting Insecure Direct Object References to Access Restricted Files

During a CTF competition, I came across a web application that allowed users to download files by providing a file identifier as a URL parameter. This functionality caught my attention, as it might be vulnerable to Insecure Direct Object Reference (IDOR) attacks, which could potentially allow me to access restricted files.

To test for an IDOR vulnerability, I manipulated the file identifier parameter in the URL to include other file identifiers, including those that I should not have access to. For example, if the original URL was http://example.com/download?file=public-file-id, I modified it to http://example.com/download?file=restricted-file-id.

When the web application allowed me to download restricted files, it confirmed the presence of an IDOR vulnerability.

To exploit the IDOR vulnerability and retrieve the flag for the Web Exploitation challenge, I enumerated various file identifiers, attempting to find the one associated with the flag file. For example, I used the following URL: http://example.com/download?file=flag-file-id.

After submitting the crafted URL, the web application allowed me to download the content of the flag file, enabling me to obtain the flag needed to complete the challenge.

This CTF writeup highlights the importance of implementing proper access controls and authorization checks in web applications to prevent IDOR vulnerabilities. By exploiting the IDOR vulnerability, I was able to access restricted files and obtain the flag needed to complete the challenge.
