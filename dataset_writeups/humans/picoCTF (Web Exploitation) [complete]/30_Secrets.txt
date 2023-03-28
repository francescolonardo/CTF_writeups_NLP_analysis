# Analysis

If we right click -> inspect and look at the sources tab, we find that some of the assets are in a suspiciously named folder called "secret".
If we navigate to the secret suburl, we find a website that says "Finally. You almost found me. you are doing well".

We are on the right track. If we repeat the same process as before, we find that there is another suspiciously named folder, "hidden", so we navigate to it. 

We keep on repeating this process until we reach a website that says "Finally. You found me. But can you see me".

# Attack Execution

The flag is probably hidden by the css. We can just look at the HTML source to get the flag.
