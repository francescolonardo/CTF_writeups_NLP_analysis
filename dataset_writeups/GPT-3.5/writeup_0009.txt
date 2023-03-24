Title: Server-Side Request Forgery (SSRF) Attack via URL Parameter

During a CTF competition, I encountered a web application that allowed users to fetch and display web pages by specifying a URL parameter. Given the potential security risks associated with URL parameters, I suspected that the application might be vulnerable to Server-Side Request Forgery (SSRF), a type of vulnerability that allows attackers to manipulate and send unauthorized requests from the server.

To test for SSRF, I crafted a malicious URL containing a request to a vulnerable server, such as http://vulnerable-server.com/admin, and submitted it to the application's URL parameter. If the application allowed the request to execute and display the vulnerable server's response, it would confirm the presence of an SSRF vulnerability.

Upon submitting the crafted URL to the application, it indeed sent the request to the vulnerable server and displayed its response, confirming the vulnerability. To obtain the flag for the Web Exploitation challenge, I needed to use the SSRF vulnerability to access a restricted resource on the server.

After researching the server's configuration and available resources, I crafted a suitable URL containing the desired resource and submitted it to the application's URL parameter. The server successfully executed the request and displayed the flag for the Web Exploitation challenge.

This CTF writeup highlights the importance of properly securing web applications against SSRF vulnerabilities by validating and sanitizing user input, using input/output encoding, and implementing white-listing and blacklisting techniques. By exploiting the SSRF vulnerability, I was able to manipulate and send unauthorized requests from the server, access restricted resources, and obtain the flag needed to complete the challenge.
