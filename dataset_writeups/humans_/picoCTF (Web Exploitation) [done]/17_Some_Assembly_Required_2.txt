Title: Some Assembly Required 2

Upon visiting the website, it appears to just be a text-box with a form. 
After inspecting the website, I can see there's a JavaScript file. I inspect that file.
The first time I looked at it I gave up in 5 seconds. Anyways, in the const declaration one of the elements caught my attention. There is a path.
I visited that path and it gave a WebAssembly file.
Until now, it's all identical to the last challenge, except that a slightly different bas64 wasm string is downloaded.
Using a Python script I converted the string to an actual wasm file.
I translate the wasm file to wat file, then I translate it to pseudo code and analyze the result. Note that this is not C code, it is C-like code.
When compared with the decompiled wasm code for the previous challenge, only some lines are new/changed at the end of the `copy` function. So we can assume that the magic happens in the `copy`.
We can see that this new version includes some extra logic.
What seems to be happening here is that the characters from the flag are getting XORed with 8 before being saved at offset 1072+. We can also see that the string that `check_flag()` uses to compare the user input to the expected flag (at offset 1024+) doesn't contain the flag in clear anymore.
I copied the variable content which can be seen from the decoded base64 text into CyberChef.
I used the magic block to search for `picoCTF` and sure enough it found the flag. Apparently, the decoding is a XOR with 8.
