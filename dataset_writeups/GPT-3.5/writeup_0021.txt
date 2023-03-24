Title: SQL Injection in Search Feature

During a CTF competition, I encountered a web application that included a search feature allowing users to search for content on the website. Given the potential security risks associated with user input, I suspected that the application might be vulnerable to SQL Injection, a type of vulnerability that allows attackers to inject SQL code into a query and manipulate the database.

To test for SQL Injection, I entered a malicious payload containing SQL code into the search box, such as ' or 1=1;--, which would cause the application to return all results, regardless of the input.

Upon submitting the payload, the application returned all results, confirming the presence of an SQL Injection vulnerability. To obtain the flag for the Web Exploitation challenge, I needed to use the SQL Injection vulnerability to extract sensitive information from the database.

After researching the application's database structure and table names, I crafted a suitable payload containing SQL code that would extract sensitive information from the database, such as UNION SELECT column_name FROM information_schema.columns WHERE table_name = 'users';. This payload allowed me to identify the names of columns in the 'users' table, such as 'username' and 'password', which contained the sensitive information.

Using the obtained column names, I crafted a second payload containing SQL code that would extract the usernames and passwords of all users in the 'users' table, such as UNION SELECT username, password FROM users;. This payload allowed me to obtain the sensitive information required to complete the Web Exploitation challenge.

This CTF writeup highlights the importance of properly securing web applications against SQL Injection vulnerabilities by implementing proper input validation and output encoding controls, using prepared statements and parameterized queries, and validating user input. By exploiting the vulnerability, I was able to extract sensitive information from the database, complete the Web Exploitation challenge, and demonstrate the potential risks associated with SQL Injection.
