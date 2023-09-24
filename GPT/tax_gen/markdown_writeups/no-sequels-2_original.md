# No Sequels 2
This was the same task as before but here we had to use blind NoSQL injection in order to fetch all of the pasword's characters by using the payload above. E.g.
```
{"username": "admin", "password": {"$gt": "a"}} -> true
{"username": "admin", "password": {"$gt": "z"}} -> false
```

By bruteforcing all characters we get the password `congratsyouwin` and then the flag: **actf{still_no_sql_in_the_sequel}**

Solving script: [./NoSequels2/solve.py](./NoSequels2/solve.py)
