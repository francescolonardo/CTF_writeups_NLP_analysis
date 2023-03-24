# Overview
Passing this level is super easy. Use the same shell as before.

# Analysis
Say the file name of your shell is shell.php. Rename it to shell.php%00.jpg. 

# Attack Execution
When submitted, the .jpg file extension will be dropped due to the preceding nullbyte. Once the file has uploaded, click it.
