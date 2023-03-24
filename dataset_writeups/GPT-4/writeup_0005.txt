Title: Exploiting File Upload Vulnerability to Execute Code

In a CTF challenge, I encountered a web application that allowed users to upload images as part of their profile. Upon examining the upload functionality, I noticed that the application seemed to perform only basic checks on the uploaded files, such as validating the file extension.

I suspected that the file upload feature might be vulnerable to a code execution attack, so I decided to craft a malicious image file that contained embedded PHP code. To do this, I created a new image file with a PHP script inserted at the beginning, which would execute when the server processed the file.

With the malicious image file prepared, I uploaded it to the web application using the profile image upload feature. After the file was successfully uploaded, I navigated to the server's directory where the uploaded images were stored.

By accessing the uploaded image file directly through its URL, I was able to trigger the execution of the embedded PHP code. The PHP script revealed sensitive information, including the location of the flag for the Web Exploitation challenge.

This CTF writeup emphasizes the importance of implementing secure file upload mechanisms, including thorough validation and sanitization of uploaded files. By exploiting the file upload vulnerability, I was able to execute arbitrary code on the server and gain access to sensitive information needed to complete the challenge.
