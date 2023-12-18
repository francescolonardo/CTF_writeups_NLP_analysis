Title: Gobustme ?

The main idea is to bruteforce directories and files hidden in a website.

We go to the URL and notice the Ghostbuster theme song, except "Ghostbusters" is replaced with "Gobuster".

The site links Gobuster which explains what kind of software it is.
This is a personal preference but DirBuster is a GUI while Gobuster is a CLI which makes DirBuster slightly more beginner friendly.

At the bottom of the website, common.txt is provided. This is a wordlist for possible lists to brute force.

Set up DirBuster by configuring it to go to the website and use common.txt as the wordlist. If your computer can handle it, check off "Go Faster". 

After running for a bit, DirBuster will give all the results. 

Upon visiting /hide we see the message "It was well hidden isn't it?" and we get the flag.
