# Analysis
For this challenge, we use burp to capture the post request sent to the server when trying to upload our php shell script and change the ‘content-type’ from ‘application/x-php’ to ‘image/jpeg’. This will trick the server into accepting the upload, thinking it’s a jpg file.

# Attack Execution
Click icon on our file and, like before, inject our command into the url:
http://challenge01.root-me.org/web-serveur/ch21/galerie/upload/gsejso5erm5ahvm8i561a9tdh7//shell.php?command=cat%20../../../.passwd
