## GETS Request
> Solved By : thewhiteh4t

* The challenge hints at memory issues
* we can enter an integer and the web app sends a reply
* there are few checks which the web app makes:

```javascript
if(!req.query.n) {
    res.status(400).send('Missing required parameter n');
    return;
}
```
* so `n` cannot be blank

```javascript
const BUFFER_SIZE = 8;

if(req.query.n.length > BUFFER_SIZE) {
    res.status(400).send('Requested n too large!');
    return;
}
```

* so max length of `n` can be `8`
* the web app does not check for duplicate parameters, so we can send another n along with the first

![](https://i.imgur.com/wyyLaq7.png)