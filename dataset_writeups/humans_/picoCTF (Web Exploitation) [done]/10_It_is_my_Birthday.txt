Title: It is my Birthday

We have a website with the possibility to upload two PDF file.
The description of the challenge states: "I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website.".
So, we're dealing with a hash collision problem.
Nowdays it's trivial to generate a MD5 collision of two images / PDF files.
Take any two PDFs of different contents, we can make them have the same MD5 hash.
I use a Python script to generate two PDF with the same MD5 hash.
After we've generated the two colliding PDFs, uploading them and the website redirected to the source code.
The flag can be found in a comment at the end of the code, at line 37.
