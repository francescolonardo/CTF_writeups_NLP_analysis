Title: Web Gauntlet 2

The attached website gives us a standard login form. If we enter credentials we even get the SQL query run on the server. 
So we can deduce the site is vulnerable to SQL injection.
Looking at the filter link we can see what we must avoid when crafting our SQL injection.
According to `filter.php` the application filters are the following: `or and true false union like = > < ; -- /* */ admin`.
We know that the username field must be "admin", but entering it as plaintext gets blocked, as we have seen. To bypass this we can simply use the `||` joiner (not filtered) with a final value for the username field of `ad'||'min`.
For the password field we must simply provide something that returns true. The most common one used is `' OR '1'='1`, but `OR` is filtered as seen. Instead we can craft a true statement using `IS` or `IS NOT` such as `a' IS NOT 'b` which is also true.
Using the final values of username and password for login we get the message "Congrats! You won! Check out `filter.php`".
Finally reloading the page gives us its source code with the flag.
