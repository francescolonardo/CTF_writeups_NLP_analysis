Title: Command Injection via Unsuspecting Image Conversion

In one of the CTF challenges, I encountered a web application that allowed users to upload images and convert them to different formats. The application seemed to use a command-line tool on the server-side to perform the conversion process. This piqued my interest, as it could potentially be vulnerable to command injection attacks.

To test this hypothesis, I decided to inject a command into the image conversion parameters. The application allowed users to choose the output format for the converted image. I crafted a payload that included a semicolon to separate the original conversion command from my injected command, which in this case was to list the contents of the server's directory.

For example, if the original command was convert input.jpg output.png, my payload would look like convert input.jpg output.png; ls. This would execute both the conversion command and the injected command to list the directory contents.

After submitting the payload through the image conversion form, I noticed that the application returned the output of the ls command, revealing the contents of the server's directory. This confirmed that the application was vulnerable to command injection.

By further exploring the server's directory structure and executing additional commands, I was able to locate the flag for the Web Exploitation challenge.

This CTF writeup underscores the importance of properly validating and sanitizing user input, especially when interacting with command-line tools on the server-side. By exploiting the command injection vulnerability, I was able to execute arbitrary commands on the server and discover the flag needed to complete the challenge.
