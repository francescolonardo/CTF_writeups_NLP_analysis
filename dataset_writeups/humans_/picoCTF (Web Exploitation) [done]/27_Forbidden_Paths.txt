# Overview

This website has the useful feature of reading any file we want it too, given its path.

# Analysis

With file paths, a preceeding ./ means the current directory, and ../ means the enclosing directory. 

# Attack Execution

Since we know that we are in /usr/share/nginx/html/, and want to access /flag.txt, we can just use the path ../../../../flag.txt to read the flag.
