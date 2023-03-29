Title: Remote File Inclusion (RFI) Attack via URL Parameter

During a CTF competition, I encountered a web application that allowed users to display and download files by specifying a URL parameter. Given the potential security risks associated with URL parameters, I suspected that the application might be vulnerable to Remote File Inclusion (RFI), a type of vulnerability that allows attackers to include and execute external files on the server.

To test for RFI, I crafted a malicious URL containing a reference to an external file, such as http://malicious-server.com/malicious.php, and submitted it to the application's URL parameter. If the application allowed the file to be included and executed on the server, it would confirm the presence of an RFI vulnerability.

Upon submitting the crafted URL to the application, it indeed included and executed the malicious file on the server, confirming the vulnerability. To obtain the flag for the Web Exploitation challenge, I needed to use the RFI vulnerability to access and execute a specific file on the server.

After researching the server's configuration and available files, I crafted a suitable URL containing the desired file and submitted it to the application's URL parameter. The server successfully included and executed the file, displaying the flag for the Web Exploitation challenge.

This CTF writeup highlights the importance of properly securing web applications against RFI vulnerabilities by validating and sanitizing user input, using whitelisting and blacklisting techniques, and implementing input/output encoding. By exploiting the RFI vulnerability, I was able to include and execute external files on the server, access restricted files, and obtain the flag needed to complete the challenge.
