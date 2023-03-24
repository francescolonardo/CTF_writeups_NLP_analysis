Title: Server-Side Template Injection Leads to Remote Code Execution

During a CTF event, I came across a web application that utilized server-side templates to dynamically generate web pages based on user input. I suspected that the application might be vulnerable to server-side template injection (SSTI), which could potentially lead to remote code execution.

To test for SSTI, I submitted a crafted input string that included template syntax to evaluate a simple expression, such as {{7*7}}. Upon processing the input, the application returned a web page that displayed the result of the evaluated expression, 49, indicating that the application was indeed vulnerable to SSTI.

To further exploit the vulnerability, I crafted a more complex payload that would execute arbitrary code on the server. In this case, I used a Python-based template engine, such as Jinja2, and submitted the following payload:

```
{{ ''.__class__.__mro__[1].__subclasses__()[40]('/bin/cat flag.txt',shell=True,stdout=-1).communicate()[0].strip() }}
```

This payload leveraged the template engine's built-in functionality to execute the cat command on the server, reading the contents of the flag.txt file.

Upon submitting the crafted payload, the application returned the contents of the flag.txt file, allowing me to complete the Web Exploitation challenge.

This CTF writeup emphasizes the importance of properly securing server-side template engines and validating user input to prevent SSTI vulnerabilities. By exploiting the SSTI vulnerability, I was able to execute remote code on the server and obtain the flag needed to complete the challenge.
