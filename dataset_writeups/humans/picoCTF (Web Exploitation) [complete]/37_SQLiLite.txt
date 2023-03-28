Title: SQLiLite

Connecting to the website will give us a login form.

In the hints it is given the user is “admin”. So, let’s test it:
```
username: admin
password: admin
```
Login failed.

The input we give is entering into the SQL command. So, we have to use SQL injection techniques to exploit this. I’m trying a common SQli payload: admin' or 1=1--

Basically, we are passing the SQL commands condition and setting our own condition. Through this we can login as “admin”.

Through adding the “ — “ we comment the remaining part of SQL command. And “or 1=1” sets as logical condition to pass the command.

Now we can see that we are logged in, but the flag is hidden. I checked the source code of the page. We got the flag.
