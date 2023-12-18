Title: Command Injection via Unsanitized User Input

During a CTF competition, I discovered a web application that executed system commands based on user input. This functionality caught my attention, as it might be vulnerable to Command Injection attacks, which could potentially allow me to execute arbitrary commands on the server.

To test for a Command Injection vulnerability, I manipulated the user input field by appending a command separator, such as ; or &&, followed by an arbitrary command. For example, if the original input was ping example.com, I modified it to ping example.com; ls.

When the web application executed the appended command and displayed the output, it confirmed the presence of a Command Injection vulnerability.

To exploit the Command Injection vulnerability and obtain the flag for the Web Exploitation challenge, I crafted an input that would execute a command to read the content of the flag file. For example, I used the following input: ping example.com; cat /path/to/flag.txt.

After submitting the crafted input, the web application executed the command and displayed the content of the flag file, allowing me to obtain the flag needed to complete the challenge.

This CTF writeup emphasizes the importance of properly sanitizing and validating user input in web applications to prevent Command Injection vulnerabilities. By exploiting the Command Injection vulnerability, I was able to execute arbitrary commands on the server and obtain the flag needed to complete the challenge.
