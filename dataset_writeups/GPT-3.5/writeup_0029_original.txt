Title: XML External Entity (XXE) Injection in File Upload

During a CTF competition, I encountered a web application that included a file upload feature allowing users to upload files to the server. Given the potential security risks associated with XML External Entity (XXE) injection vulnerabilities, I suspected that the application might be vulnerable to XXE injection attacks.

To test for XXE injection, I uploaded a malicious XML file containing a payload, such as <!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]> <foo>&xxe;</foo>, which would allow me to read the contents of the server's passwd file.

Upon uploading the file, the application accepted it and stored it on the server. To trigger the XXE payload, I entered a payload containing the file upload URL and an XML document reference, such as http://example.com/uploads/malicious.xml, which would trigger the XXE payload and allow me to read the contents of the passwd file.

This payload allowed me to obtain sensitive information, such as system configuration files, database credentials, and other sensitive information.

This CTF writeup highlights the importance of properly securing web applications against XXE injection vulnerabilities by implementing proper input validation and output encoding controls, using parameterized queries, and validating user input. By exploiting the vulnerability, I was able to read sensitive information from the server, demonstrate the potential risks associated with XXE injection, and recommend proper countermeasures to prevent these types of attacks.
