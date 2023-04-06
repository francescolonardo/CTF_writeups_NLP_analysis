Title: dont-use-client-side

Opening the website greets us with a login page, requiring credentials.
As referenced by the challenge name, we assume that the check for the validity of the credentials is checked client side, and hence can be reversed to obtain the correct password.
The first obvious thing to do as nothing else is look at the page source code hoping to find anything important. And boom, we win the lottery!
We got that the password is checked split in parts against the flag itself divided in parts.
We use a bash script to join them together and obtain the flag.
