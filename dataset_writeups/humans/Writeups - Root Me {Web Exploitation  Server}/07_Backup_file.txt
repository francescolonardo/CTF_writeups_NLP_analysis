# Overview
This one is a bit trickier. You are given a username and password field, but the intended solution doesn’t include any improper text sanitization. 

# Analysis
If you are a vim god, you would know that vim backup files are stored as the original name of the file, with a tilde character at the end of the filename.

# Attack Execution
Knowing this, just navigate to /index.php~, and download the file. There, you will find the password.
