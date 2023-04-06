# Analysis
PHP filters are used to validate and sanitize external input.
There are number of filters that can be applied. One built-in filter is convert.base64-encode and convert.base64-decode, the former of which will be used in this exploit.
It will go like php://filter/convert.base64-encode

php://filter/convert.base64-encode/resource allows us to read any source of a php file. It forces PHP to base64 encode the file before it is used in the require statement. From there decoding the base64 string will give us the source code for whichever php file is called by parameter ‘resource’.

# Attack Execution
We continue guessing helpful php files such as config.php
http://challenge01.root-me.org/web-serveur/ch12/?inc=php://filter/convert.base64-encode/resource=config.php
