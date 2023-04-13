Title: Empire1

# Overview
First thing we notice when we open the homepage is register and login pages, but they doesnt seem to be vulnerable to sqli so we create a user and we login.

# Attack Execution
Lets see that create todo page, if we try to inject a simple ' in the todo we get an internal server error so we know that probably we can inject sql. In fact if we try a simple a' OR '1'='1 the query is executed and in todo list we can see the output 1.

# Analysis
If we play a little with queries we will find that a good method to inject a query is this a' || (some_query) || 'b.

Now we have to find some info about the db, in order to do that we have to undestand which dbms is being used, we try to select information_schema which is mysql but it won't work, if we try sqlite_master it will work so we print some information and then we can start printing the good stuff.
The challenge description clearly says us to find our secret so if we print the secret "column" of every user selected by his id we are gonna find ours and with it our flag.
