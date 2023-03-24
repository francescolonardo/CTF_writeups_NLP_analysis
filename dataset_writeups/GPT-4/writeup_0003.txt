Title: Exploiting Open Redirect Vulnerability for Phishing

In a recent CTF competition, I came across a web application that allowed users to share links to external websites. The application used a redirect mechanism to track clicks and count the number of visits for each shared link. However, upon further investigation, I found that the application was vulnerable to an open redirect attack.

The application's redirect mechanism used a URL parameter, redirect, to specify the target destination. By crafting a malicious URL with the redirect parameter set to a phishing site, I was able to exploit the open redirect vulnerability.

To demonstrate the attack, I created a URL with the redirect parameter set to a phishing site that mimicked the application's login page. When unsuspecting users clicked on the malicious link, they were redirected to the phishing site, which prompted them to enter their login credentials.

By collecting the submitted credentials, I was able to gain unauthorized access to the user accounts and complete the Web Exploitation challenge by finding the flag stored in a restricted area.

This CTF writeup highlights the importance of properly validating and sanitizing user input, especially when dealing with URL parameters. By exploiting the open redirect vulnerability, I was able to launch a phishing attack and gain unauthorized access to user accounts.
