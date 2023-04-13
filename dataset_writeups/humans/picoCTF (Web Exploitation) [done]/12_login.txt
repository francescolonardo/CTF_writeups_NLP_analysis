Title: login

On first inspection, we faced with a login screen.
It seems like SQL injection, because "isn't that what always happens with logins in CTFs?". However, it's a lot simpler than that. After navigating to the website source, we encounter a .js file. After a pretty printing, it's just vanilla JavaScript.
The important part of the code is in line 12, where it's checking for a username and password that has been turned into base64 from ASCII via the `btoa()` method, which is reversible with the `atob()` method. The password itself is the flag when decoded.
Opening the Chrome console and undoing the encoding, results in the flag. If you're not convinced it's the real flag, you can decode the username (admin) and input both into the login form, which results in an alert announcing the flag.
