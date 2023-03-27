Title: SSRF Attack to Access Internal Services and Retrieve Flag

During a CTF event, I encountered a web application that allowed users to fetch the content of external websites by providing a URL. The application would then display the fetched content on the page. This functionality raised my suspicion of a potential Server-Side Request Forgery (SSRF) vulnerability, which could be exploited to access internal services or restricted content on the server.

To test for an SSRF vulnerability, I crafted a URL pointing to the local server's internal IP address and a port that was suspected to host an internal service. For example, if the original URL was https://example.com/fetch?url=https://google.com, I modified it to https://example.com/fetch?url=http://localhost:8080.

Upon navigating to the modified URL, the application returned a web page that displayed the content of an internal service running on the local server. This confirmed the presence of an SSRF vulnerability.

By further exploiting the SSRF vulnerability and accessing different internal services or restricted content on the server, I was able to locate the flag required for the Web Exploitation challenge.

This CTF writeup highlights the importance of properly validating and sanitizing user-supplied URLs in web applications to prevent SSRF vulnerabilities. By exploiting the SSRF vulnerability, I was able to access internal services and restricted content on the server, leading me to find the flag needed to complete the challenge.
