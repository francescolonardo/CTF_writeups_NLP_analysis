# Overview
Check source code.  You can see that when an option is selected, you are redirected to, for example, https://facebook.com&h=......&#8230;.

# Analysis
We need to figure out what the value followed by &h= is, so we can structure our redirect url accordingly.
Using an online md5 hash to text converter, we see the value represents the hashed value of the particular url.  MD5 hash https://google.com&#8217; and note the value.

# Attack Execution
Start tamper data and click the facebook link.  Edit the url so the website redirects to ?url=https://google.com&h=<MD5hash of https://google.com>&#8217; instead of facebook.  Then submit the page.
