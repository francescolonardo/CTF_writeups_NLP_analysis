Title: Exploiting an Open Redirect Vulnerability for Phishing Purposes

During a CTF competition, I found a web application that contained functionality allowing users to be redirected to external websites by passing a URL parameter. This functionality caught my attention, as it might be vulnerable to Open Redirect attacks, which can be used for phishing or other malicious purposes.

To test for an Open Redirect vulnerability, I manipulated the URL parameter to include external websites and observe whether the application would redirect me to those sites. For example, if the original URL was http://example.com/redirect?url=http://legitimate-site.com, I modified it to http://example.com/redirect?url=http://malicious-site.com.

When the web application redirected me to the malicious site, it confirmed the presence of an Open Redirect vulnerability.

To exploit the Open Redirect vulnerability and obtain the flag for the Web Exploitation challenge, I crafted a URL that would redirect users to a phishing site mimicking the target application, which logged user credentials. For example, I used the following URL: http://example.com/redirect?url=http://phishing-site.com.

After creating the phishing site and sharing the crafted URL, I collected user credentials and used them to log in to the target application. Once logged in, I navigated to a restricted area containing the flag needed to complete the challenge.

This CTF writeup highlights the importance of properly validating and sanitizing user input in web applications to prevent Open Redirect vulnerabilities. By exploiting the Open Redirect vulnerability, I was able to phish user credentials and obtain the flag needed to complete the challenge.
