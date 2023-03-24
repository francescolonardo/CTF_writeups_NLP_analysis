# Overview
We have url like this: http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=emotes.
The parameter galerie displays different categories.

# Analysis
We can deduce ‘galerie’ holds all the files.
Navigating to http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=,
we can see a hidden folder beginning with ’86hv’.
Move your mouse above the icon and right click, select inspect element to get the full folder name.

# Attack Execution
Navigate to http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=86hwnX2r, 
you’ll see a file password.txt. Right click and view the source code. Click the ‘password.txt’ hyperlink for the password.
