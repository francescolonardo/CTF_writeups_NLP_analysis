Title: Capturing Flags with XPath Injection in XML-Based Web Applications

During a CTF competition, I came across a web application that used XML to store and process data. The application allowed users to search for specific information through a search box. This caught my attention, as it could potentially be vulnerable to an XPath Injection attack, enabling an attacker to access sensitive data stored in the XML documents.

To test for an XPath Injection vulnerability, I submitted various XPath expressions through the search box to see if the application would evaluate them. For example, I entered the following expression: ' or '1'='1. If the application was vulnerable, it would return all the data in the XML documents.

Upon submitting the crafted input, the web application displayed all the data from the XML documents, confirming the presence of an XPath Injection vulnerability.

To exploit the vulnerability and retrieve the flag for the Web Exploitation challenge, I crafted a more specific XPath expression that would search for the flag within the XML documents. For example, I used the following expression: //flag[contains(text(), 'FLAG')].

After submitting the payload, the web application displayed the content of the flag element, allowing me to obtain the flag needed to complete the challenge.

This CTF writeup emphasizes the importance of properly validating and sanitizing user input in web applications that utilize XML and XPath to prevent XPath Injection vulnerabilities. By exploiting the XPath Injection vulnerability, I was able to access sensitive data stored in the XML documents and retrieve the flag needed to complete the challenge.
