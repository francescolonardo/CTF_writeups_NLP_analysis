Title: Abusing Open Redirect Vulnerability to Perform Phishing Attacks

During a CTF event, I encountered a web application that allowed users to input a URL, which would then redirect the user to that destination. This functionality caught my attention, as it could potentially be vulnerable to an Open Redirect attack, allowing an attacker to create malicious URLs that redirect users to attacker-controlled websites.

To test for an Open Redirect vulnerability, I crafted a URL that included a redirection to an attacker-controlled website. For example, if the original URL was https://example.com/redirect?url=https://google.com, I modified it to https://example.com/redirect?url=https://attacker.com.

Upon navigating to the modified URL, the application redirected me to the attacker-controlled website, confirming the presence of an Open Redirect vulnerability.

To exploit this vulnerability, I created a phishing page that mimicked the appearance of the original web application and hosted it on my attacker-controlled website. I then crafted a malicious URL that redirected users to my phishing page and distributed the URL to unsuspecting users. By doing so, I was able to capture their login credentials and gain unauthorized access to their accounts.

Inside one of the compromised accounts, I found the flag for the Web Exploitation challenge.

This CTF writeup emphasizes the importance of properly validating and sanitizing user-supplied URLs in web applications to prevent Open Redirect vulnerabilities. By exploiting the Open Redirect vulnerability, I was able to perform phishing attacks, compromise user accounts, and obtain the flag needed to complete the challenge.
