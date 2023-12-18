Title: Irish-Name-Repo 1

When we open the site, we see the content of the main page is not very helpful. When we look at the Support page however, we see an inquiry saying:
"Hi. I tried adding my favorite Irish person, Conan O'Brien. But I keep getting something called a SQL Error."

This tells us that the site uses a SQL database. When we go to the Admin Login, we can try a basic SQL Injection to bypass the portal. Our injection is specifically having the username as ' OR 1=1-- and the password as whatever.

What is happening here is the query checks if the username is equal to nothing. Then, it checks OR 1=1. Since 1 is always going to be equal to 1, this returns true. The -- at the end simply comments out the rest of the query. This fools the server into letting us through the portal.