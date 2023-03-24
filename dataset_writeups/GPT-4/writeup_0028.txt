Title: Command Injection via Unsanitized User Input

During a CTF competition, I came across a web application that allowed users to perform server-side actions by entering commands through a form. This caught my attention, as it might be vulnerable to command injection attacks, which could potentially allow me to execute arbitrary commands on the server.

To test for command injection vulnerability, I tried appending additional commands to the input field using common command separators such as ;, &&, or ||. For example, I entered the following input: ping 127.0.0.1; cat /etc/passwd.

When the web application executed both the ping command and displayed the content of the /etc/passwd file, it confirmed the presence of a command injection vulnerability.

To exploit the command injection vulnerability and retrieve the flag for the Web Exploitation challenge, I crafted a payload that would search for the flag within the server's file system. For example, I used the following input: ping 127.0.0.1; find / -name "flag.txt" -exec cat {} \;.

After submitting the payload, the web application executed the commands, and the content of the flag file was displayed, allowing me to obtain the flag needed to complete the challenge.

This CTF writeup underscores the importance of properly validating and sanitizing user input in web applications to prevent command injection vulnerabilities. By exploiting the command injection vulnerability, I was able to execute arbitrary commands on the server and obtain the flag needed to complete the challenge.
