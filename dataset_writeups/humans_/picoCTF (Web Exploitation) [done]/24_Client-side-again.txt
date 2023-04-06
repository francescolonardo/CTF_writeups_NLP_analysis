Title: Client-side-again

We visit the website and inspect the source code. Let's call a JavaScript beautifier in order to make the JavaScript code a bit more readable.
We see that `_0x4b5b` is a function used to obfuscate different values. It is calculated in runtime. Luckily, we can use the browser's Developer Tools console in order to evaluate the obfuscated function and read its values.
Let's replace the function calls with hardcoded values to improve readability.
So this is very similar to another challenge already seen, using `substring` to authenticate the password.
Indeed we have some substrings composing the flag. Note that there are some overlaps.
An evil way to turn this into a flag would be by transforming the JavaScript code into a Python array assignment script and executing it.
This gives us the flag at the price of allowing exec to slip into our code.
