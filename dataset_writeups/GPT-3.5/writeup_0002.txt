Title: XXE Injection to Access Server Files

During a CTF competition, I encountered a web application that parsed XML input and displayed the results to the user. Given the nature of XML parsing and processing, I suspected that the application might be vulnerable to XML External Entity (XXE) injection, a type of vulnerability that allows attackers to read arbitrary files on the server or execute remote requests.

To test for XXE injection, I crafted an XML input containing a reference to an external entity, such as <!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]> <root>&xxe;</root>. If the application parsed the input and displayed the contents of the passwd file, it would confirm the presence of an XXE injection vulnerability.

Upon submitting the crafted input to the application, it indeed displayed the contents of the passwd file, confirming the vulnerability. To obtain the flag for the Web Exploitation challenge, I needed to use the XXE injection vulnerability to read a specific file on the server.

After crafting a suitable payload and choosing the target file, I submitted the input to the application, which executed the XXE injection and displayed the contents of the file, including the flag for the Web Exploitation challenge.

This CTF writeup highlights the importance of properly securing web applications against XXE injection vulnerabilities by validating and sanitizing XML input, disabling external entity references, and restricting file system access. By exploiting the XXE injection vulnerability, I was able to read arbitrary files on the server, extract sensitive data, and obtain the flag needed to complete the challenge.
