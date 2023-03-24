Title: "File Inclusion Vulnerability in File Upload Feature"

During a CTF competition, I discovered a file inclusion vulnerability in a file upload feature of a web application. The application allowed users to upload files, which were stored on the server and accessible via a URL. However, the application did not properly validate the file name and extension, allowing me to upload and execute arbitrary files on the server.

To exploit the vulnerability, I uploaded a PHP shell script disguised as a JPG file. The application stored the file on the server and generated a URL for the file. I then accessed the URL, which executed the PHP shell script on the server, giving me full control over the system.

With control over the server, I was able to perform various actions, such as accessing sensitive files, modifying the website content, and compromising user data. To mitigate this vulnerability, I recommended that the application implement proper file validation and restriction techniques to prevent file inclusion attacks.

This CTF writeup highlights the importance of properly securing file upload features in web applications by implementing proper file validation and restriction techniques to prevent file inclusion attacks. By exploiting the vulnerability, I was able to demonstrate the potential risks associated with a file inclusion vulnerability in a file upload feature and recommend proper countermeasures to prevent these types of attacks.
