Title: XML External Entity (XXE) Attack to Access Sensitive Files

During a CTF event, I came across a web application that allowed users to import and export data using XML files. This functionality raised the possibility of an XML External Entity (XXE) vulnerability, which could be exploited to access sensitive files on the server or perform other malicious actions.

To test for an XXE vulnerability, I crafted a malicious XML file that included an external entity pointing to a sensitive file on the server, such as /etc/passwd. The XML file looked like this:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >
]>
<foo>&xxe;</foo>
```

I then uploaded the crafted XML file using the import feature provided by the web application. Upon processing the XML file, the application returned an error message that included the contents of the /etc/passwd file, confirming the presence of an XXE vulnerability.

By further exploiting the XXE vulnerability and accessing other sensitive files on the server, I was able to locate the flag required for the Web Exploitation challenge.

This CTF writeup highlights the importance of securing XML parsers and properly handling user-supplied XML files in web applications. By exploiting the XXE vulnerability, I was able to access sensitive server files and obtain the flag needed to complete the challenge.
