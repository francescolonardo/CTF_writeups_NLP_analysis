Title: Irish-Name-Repo 2

This site looks a lot like the one from Irish-Name-Repo 1, yet once we try this same SQL Injection of ' OR 1=1-- here, we get nothing but a page that says SQLi detected.

After some playing around, we can figure out that the filter detects several keywords, including UNION which was the solution for last year's SQLi filter challenge.

However, after some blind SQLi, we bypass the filter by setting the username to admin'-- and the password to whatever. We are guessing that the username here should be admin and then commenting out the rest so that the password is not checked.