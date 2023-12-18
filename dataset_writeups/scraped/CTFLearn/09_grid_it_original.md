Title: Grid It!

We are given a register/login panel on a webpage. After logging in, we see a 2D plane where we can add or remove points. Requests go through "controller.php?action=", with various actions available.

We notice a PHP serialized object when deleting points. We try SQL Injection by modifying the object and all points disappear. We observe that the delete() function is invoked on the point object, hinting at PHP Object Injection. However, the classes containing the ::delete() method (Phar and PharData) seem useless for this task.

We return to SQL Injection, aiming for Blind SQL Injection since there's no output. Our goal is to fetch table and column names inside the database. We create queries with conditions based on the comparison of ASCII codes of characters in the desired data. We perform a binary search to find the correct characters and retrieve the entire name. We find two tables and six columns.

We fetch the admin's password with a similar query and obtain an MD5 hash. After cracking it, we get the password: grapevine. Logging in as admin, we receive the flag: ctflearn{obj3ct_inj3ct1on}. The name is misleading as it wasn't an object injection, just object modification.
