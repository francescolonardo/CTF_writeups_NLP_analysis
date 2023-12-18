Title: Basic Injection

Just like the title said, the task involves SQL injection (SQLi), which I really have not yet studied. Let's begin.

I have a little expirience and understanding of SQL so my study was not long, the point is to make the request valid, for example 1=1 is always true, so the server will return all of the items.

This challenge is really friendly and shows what is the resulting query, which helps a lot.

We need to make the query valid, but not really a big riddle, my resulting input is '' or 'a'='a and the missing ' will be added by the server.

The payload going to pull all the data from the database. This is because the input field is not sanitized which makes the searching field vulnerable to the SQL injection. A hacker can pull all the information from a database that included sensitive data.

That’s all for the simple web challenge. Bye.
