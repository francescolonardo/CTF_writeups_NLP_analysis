Title: "Broken Access Control"

A new web application was recently deployed for a company, but the developers made a mistake by not implementing access control correctly. As a result, users can access pages and functions they should not have access to. The goal of this challenge is to exploit this vulnerability and obtain sensitive information from the application.

The first step was to identify the vulnerable pages. The main menu of the application had options for users and administrators. Accessing the administrator menu allowed for actions like adding new users, while the user menu had options for viewing and updating personal information. However, using Burp Suite to intercept the HTTP traffic showed that the application was not properly enforcing access control, as the same endpoints could be accessed regardless of the user role.

To demonstrate the exploit, a user account was used to log in and access the user menu. From there, it was possible to change the request's parameters and change the user ID to an administrator's ID. Submitting the modified request resulted in accessing the administrator's menu, revealing sensitive functions and data.

The fix for this vulnerability would involve implementing proper access control checks on the server-side, so that users can only access the pages and functions they are authorized to access based on their role.
