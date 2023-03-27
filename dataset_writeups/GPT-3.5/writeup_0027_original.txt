Title: SQL Injection in User Login

During a CTF competition, I encountered a web application that included a user login feature allowing users to login using their credentials. Given the potential security risks associated with SQL injection vulnerabilities, I suspected that the application might be vulnerable to SQL injection attacks.

To test for SQL injection, I entered a malicious payload containing a SQL injection attack into the login parameter, such as admin' --, which would cause the application to execute a valid SQL query and bypass the authentication mechanism.

Upon submitting the payload, the application logged me in as an administrator, confirming the presence of an SQL injection vulnerability. To obtain the flag for the Web Exploitation challenge, I needed to use the SQL injection vulnerability to extract sensitive information from the database.

After researching the application's database schema and structure, I crafted a suitable payload containing a script that would extract sensitive information from the database, such as admin' UNION SELECT 1,2,3,4,5,6,7 FROM sensitive_table WHERE '1'='1. This payload allowed me to extract sensitive information from the database, such as the flag for the Web Exploitation challenge.

This CTF writeup highlights the importance of properly securing web applications against SQL injection vulnerabilities by implementing proper input validation and output encoding controls, using parameterized queries, and validating user input. By exploiting the vulnerability, I was able to extract sensitive information from the database, complete the Web Exploitation challenge, and demonstrate the potential risks associated with SQL injection.
