Title: Local Authority

When you go to the website, you find a login screen.
To find out more about the inner workings of the website, we look at the source code (right-click on the page).
Nothing visible at first sight. We dive deeper and look at PHP, JavaScript and CSS files.
In `style.css` there is nothing special.
Surprisingly, some of the source codes in the `login.php` are shown to us. This is because the logic that is handling our login credentials is in the Javascript function in HTML that is echoed to us.
The function `filter()` obviously checks if the entered field contains only allowed letters. The JavaScript code following the function definition reads the entered values and passes them on to a function called `checkPassword()` which is not defined in this document. Since we are looking for JavaScript code, we look into `secure.js`.
Okay, that was not difficult. The login credentials for the website are here.
If we copy the password, go back to the login screen, enter the password together with the username, we get the flag.
