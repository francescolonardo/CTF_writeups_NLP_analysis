# Overview
The first thing we see is a text field that accepts IP addresses, pings them, and returns the output as if it was a shell command.

# Analysis
Seeing the output look like it came from a unix shell, trying to put commands such as ls sounds like a good idea, but there seems to be some sanitization. To get around this, you can put in an IP address, along with another command using the & symbol.

# Attack Execution
In the description of the challenge, it says the flag is in the index.php file, but if you look at the source code of the page, there’s nothing there. 
Assuming that file is on the compromised service, we can inject a command to cat the file, and grep for the flag.
The command I used was: 127.0.0.1 & cat index.php | grep flag