# Overview
This challenge really irritated me because it took me 3 different plugins to find one that would work. Once I did, solving the challenge is a no-brainer.

# Analysis
Click on ‘saved email addresses’, we get an error that says we must be admin.
Checking the url:
http://challenge01.root-me.org/web-serveur/ch7/?c=visiteur
But simply replacing ‘visiteur’ with ‘admin’ we get an error that says there’s an issue with the cookie value.

# Attack Execution
Install the firefox plugin ‘Live HTTP Headers’ and click the ‘Saved email addresses’ link again. In live http headers, you can see the cookie: ch7=visiteur. Click ‘replay’ and change ‘visiteur’ to ‘admin’, then replay again. In the browser click the link once more to find the validation password.
