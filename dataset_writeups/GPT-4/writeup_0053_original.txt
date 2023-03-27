Title: "Broken Password"

In this CTF challenge, we are provided with a login page that asks for a username and password. We are given a hint that the password may have been broken, and we are asked to find the password.

Upon inspecting the page source, we can see that there is a hidden input field named "flag", with a value of "0". We can try changing this value to "1" and submitting the form, but we receive an error message that the password is incorrect.

Next, we can try a SQL injection attack by entering a username of "' OR 1=1 --" and leaving the password field blank. This will result in a successful login, as the injected SQL statement will always evaluate to true, bypassing the password check.

We are now presented with a welcome page that displays the flag. We can submit the flag to complete the challenge.

Overall, this challenge highlights the importance of secure coding practices and input validation to prevent SQL injection attacks.
