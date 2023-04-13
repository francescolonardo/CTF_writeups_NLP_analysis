# Overview
There is a zip file upload.

# Attack Execution
I wrote a .php file, compressed to .zip file, uploaded.

# Analysis
Report 403 code, because the php file cannot be accessed, only txt/jpg can be.

# Attack Execution
Create a soft link in kali to a .txt file, and then use the zip command compression symbol link file. Uploaded.

# Analysis
Found that the .txt file is larger in size, clicking on the .txt file we'll get the index.php code.
