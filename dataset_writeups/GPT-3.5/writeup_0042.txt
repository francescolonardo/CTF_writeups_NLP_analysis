Title: "LFI Vulnerability in a File Upload Feature"

During a CTF competition, I discovered a Local File Inclusion (LFI) vulnerability in a file upload feature on a web application. The application allowed users to upload files, which were then accessible through a download link on the website. However, the application did not properly sanitize the user input, allowing me to upload a malicious file with a crafted file name that would allow me to access sensitive system files.

To exploit the vulnerability, I uploaded a PHP file with a crafted name containing the relative path to sensitive system files, such as configuration files or password hashes. By accessing the download link for the uploaded file, the application would include the contents of the sensitive file in the server response, allowing me to view and potentially modify its contents.

Using this LFI attack, I was able to gain access to sensitive information and potentially compromise the security of the web application and the underlying system.

To mitigate this vulnerability, I recommended that the application implement proper input validation and sanitation techniques to prevent LFI attacks. The application should also implement proper file handling techniques, such as enforcing strict file type and size limits and storing files outside of the web root directory to prevent access to sensitive system files.

This CTF writeup highlights the importance of properly securing file upload features in web applications by implementing proper input validation and sanitation techniques to prevent LFI attacks. By exploiting the vulnerability, I was able to demonstrate the potential risks associated with an LFI vulnerability and recommend proper countermeasures to prevent these types of attacks.
