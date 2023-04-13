Title: Web Gauntlet 3

The challenge is the exact same as Web Gauntlet 2 but we know have a 25 total character limit for our username and passoword field entry.

Thankfully our solution for Web Gauntlet 2 is under this limit and also works for this challenge so check the writeup for that out here to get a more detailed explanation and use the same values.

Final values for login:
```
username: ad'||'min
password: a' IS NOT 'b
```

After inputting these values for username and password we login and get the message "Congrats! You won! Check out filter.php". Reloading the filter.php file we get the source code for the challenge along with the flag in the comments just as for Web Gauntlet 2.
