Title: XXE Attack to Exfiltrate Sensitive Data from Web Application

During a CTF event, I encountered a web application that processed XML data from users, which caught my attention because it might be vulnerable to XML External Entity (XXE) attacks. An XXE attack can allow an attacker to access sensitive data or execute commands on the server.

To test for an XXE vulnerability, I crafted an XML payload containing an external entity that would reference a local file on the server, such as /etc/passwd. For example, I created the following payload:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >
]>
<foo>&xxe;</foo>
```

I submitted the payload to the web application and observed the response. If the application returned the content of the /etc/passwd file, it would confirm the presence of an XXE vulnerability.

To exploit the XXE vulnerability and obtain the flag for the Web Exploitation challenge, I modified the payload to reference the server's file system location containing the flag. For example:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///path/to/flag.txt" >
]>
<foo>&xxe;</foo>
```

After submitting the modified payload, the web application returned the content of the flag file, allowing me to obtain the flag needed to complete the challenge.

This CTF writeup emphasizes the importance of securely handling and processing XML data in web applications to prevent XXE vulnerabilities. By exploiting the XXE vulnerability, I was able to access sensitive data on the server and obtain the flag needed to complete the challenge.
