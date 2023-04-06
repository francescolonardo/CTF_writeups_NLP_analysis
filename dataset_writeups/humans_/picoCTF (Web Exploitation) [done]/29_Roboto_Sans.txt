# Overview

The challenge name seems to be either an allusion to the text font Roboto or /robots.txt.
As investigating the text font files seems more complicated, let's first look at /robots.txt.

# Analysis

The text in here disallow looks suspicious.

The double equal sign suggests that it's base 64. However, if we try to decode it with an online decoder, it seems like the base 64 is a little malformed. As the base 64 text spans across three lines, it suggests that it is actually three separate strings.

# Attack Execution

If we decode each line separately, we find that the second line gives us a valid path, specifically js/myfile.txt. If we navigate to the suburl, we get the flag.
