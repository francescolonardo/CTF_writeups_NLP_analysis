Title: Cross-Site Scripting (XSS) Attack via Form Input

During a CTF competition, I encountered a web application that allowed users to submit feedback through a form. Given the potential security risks associated with form input, I suspected that the application might be vulnerable to Cross-Site Scripting (XSS), a type of vulnerability that allows attackers to inject and execute malicious scripts in the user's browser.

To test for XSS, I crafted a malicious input containing a script, such as <script>alert('XSS');</script>, and submitted it to the application's form. If the application allowed the script to execute and display the alert message, it would confirm the presence of an XSS vulnerability.

Upon submitting the crafted input to the application, it indeed executed the script and displayed the alert message, confirming the vulnerability. To obtain the flag for the Web Exploitation challenge, I needed to use the XSS vulnerability to steal the user's session cookie and impersonate them.

After crafting a suitable payload containing a script to steal the session cookie, I submitted it to the application's form. The script successfully executed and sent the user's session cookie to a remote server controlled by me, allowing me to impersonate the user and obtain the flag for the Web Exploitation challenge.

This CTF writeup highlights the importance of properly securing web applications against XSS vulnerabilities by validating and sanitizing user input, using content security policies, and implementing input/output encoding. By exploiting the XSS vulnerability, I was able to inject and execute malicious scripts, steal sensitive information, and obtain the flag needed to complete the challenge.
