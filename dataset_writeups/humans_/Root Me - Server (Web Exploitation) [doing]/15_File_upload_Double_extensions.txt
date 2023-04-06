# Overview
Referring to the documentation provided along with this challenge, I wrote a quick php script and saved it as php_shell.php.jpg.

# Analysis
Sometimes you can trick the web server into accepting your php file by adding an acceptable file extension (jpg, png, gif) to the end of the php file extension.

# Attack Execution
After uploading the file, we navigate to it and inject our command into the url.
‘…..php_shell.php.jpg?command=cat ../../../.passwd’
