## EXtravagant

> Solved By : nigamelastic
![](https://i.imgur.com/rmw9shq.png)

The challenge mentions the following:

```
The flag is in /var/www
```

on accessing the website we see a normal interface with xml parsing as a service

![](https://i.imgur.com/iWDrdSZ.png)

from the mentioning of XML it seems that this might be an XXE

Since we already know the locaiton of the flag I used the following payload:

![](https://i.imgur.com/sqelqWg.png)

I simply uploaded it to the trial tab:

![](https://i.imgur.com/h9WG0EH.png)

![](https://i.imgur.com/90bhiq3.png)

and then used view XML tab to view my xml

![](https://i.imgur.com/z5PUs40.png)

This would give flag

![](https://i.imgur.com/Tp2Wy2s.png)
