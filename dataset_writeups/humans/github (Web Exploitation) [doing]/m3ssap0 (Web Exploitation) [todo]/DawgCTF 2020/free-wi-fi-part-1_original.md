## Free Wi-Fi Part 1

* **Category:** web/networking
* **Points:** 50

### Challenge

> People are getting online here, but the page doesn't seem to be implemented...I ran a pcap to see what I could find out.
> 
> http://freewifi.ctf.umbccd.io/
> 
> Authors: pleoxconfusa and freethepockets

### Solution

The HTML code of the page is the following.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>
Guest Sign In Portal
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

      <h1>Sorry!</h1>

      <br><br>

      <div align="left" style="background-color: lightgrey; width: 500px;  padding: 50px;  margin: 20px;">
	<h3 style="color:blue;">Guest login</h3>
      	<p class="space-above"><strong>Guest sign in portal is not yet implemented.</strong></p>
      </div>

    </div>
  </div>
</div>



    
    <script src="/static/bootstrap/jquery.min.js?bootstrap=3.3.7.1.dev1"></script>
    <script src="/static/bootstrap/js/bootstrap.min.js?bootstrap=3.3.7.1.dev1"></script>
  </body>
</html>
```

So there is anything to authenticate there.

Analyzing the [PCAP file](free-wifi.pcap) you can discover on packet #6 the existence of `https://freewifi.ctf.umbccd.io/staff.html` web page.

Connecting to it, you will discover the flag.

```
DawgCTF{w3lc0m3_t0_d@wgs3c_!nt3rn@t!0n@l}
```
