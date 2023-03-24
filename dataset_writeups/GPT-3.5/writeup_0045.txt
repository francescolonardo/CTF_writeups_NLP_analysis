Title: "Cross-Site Request Forgery (CSRF) in a Contact Form"

During a CTF competition, I discovered a Cross-Site Request Forgery (CSRF) vulnerability in a contact form of a web application. The contact form allowed users to submit messages to the website owner, but the application did not implement proper CSRF protections.

I crafted a malicious web page that included a hidden form that submitted a message to the contact form on behalf of the victim user. By tricking the victim user into visiting my web page, I was able to submit a message to the website owner with the victim user's credentials.

This vulnerability could have allowed an attacker to submit malicious messages to the website owner, manipulate user data, or launch further attacks on other systems connected to the server.

To mitigate this vulnerability, I recommended that the application implement proper CSRF protections, such as adding a random token to each form submission and validating the token on the server side. The application should also add additional user authentication measures, such as requiring users to enter their password to submit sensitive information.

This CTF writeup highlights the importance of properly securing web applications against CSRF attacks by implementing proper CSRF protections and user authentication measures. By exploiting the vulnerability, I was able to demonstrate the potential risks associated with a CSRF vulnerability and recommend proper countermeasures to prevent these types of attacks.
