# Overview

This is the final WebAssembly challenge. The process that I used to solve this challenge can also be applied to all the other ones as well, so I’ll just outline how I solved this one.

I’m not very good at reverse engineering, and only have a very rudimentary understanding of WASM in general so I’m sure there’s a better way to go about this.

# Analysis

The basic flow of the challenge is that you enter in a flag and it checks if its the correct flag.

The JavaScript on the page interacts with a WASM program by first copying over each character in the flag into memory using the copy_char() function. Afterward, it calls check_flag() and receives a boolean, depending on whether the flag was valid or not.

Reverse Engineering

Google Chrome has one of the best tooling suites ever. This extends to WASM, where there is a debugger that disassembles the compiled WASM binaries into WebAssembly Text Format (WAT) and allows you to add breakpoints wherever you want. Thus the process of vaguely figuring out how it works is quite simple: all you need to do is to put breakpoints where you think something happens and you can inspect local variables at that breakpoint.

My process was even more simple. I was able to identify that the code was looping through the entered value (by putting in picoCTF{ as a prefix and putting random characters afterward) and returning when a character didn’t match. For this specific challenge, it compares two characters at a time, in contrast to the previous challenge which only compared one at a time.

(Smart) Brute Force

The fact that this is a short circuit allows us to do a side channel attack on the checking process. To speed this up, we can add snippets of code that increments a counter whenever you get a character correct and resets that counter whenever you call the function. Knowing how many characters we got correct allows us to brute force the flag two characters at a time.

You can see now how this now reduces to brute forcing two characters at a time, since we can start with guessing the first two. After we know those two characters are correct, we can guess the next two, then the next two… until we get to the end.

The only issue now is how we’ll add the code in. I don’t know how to write WebAssembly at all, and learning it seemed to be quite a steep curve. Instead of writing the WASM code myself, I found that you can compile C to WASM and then just copy those code snippets. I used WasmFiddle for this purpose.


The part that declares the memory location for the global variable is (data (i32.const 16) "\00"), and its clear that the offset of this memory location is 16. We can change this to whatever we want as long as we change the appropriate offsets in the rest of the code.

We also want to reset the global variable between runs, so I also compiled a snippet that set the variable to 0.

I identified a suitable location to add the code snippets, which is right after a eq operation in the program. Using the information gained from putting a breakpoint there, I could tell that the inserted code would only run if the character matched.

Since the WASM code is really long, I’ve uploaded them as files. You can see the final patched WAT file here and the diff between the original and patched here, I used an offset location of 3000 in my patch. I used the WebAssembly Binary Toolkit (WABT) to disassemble and reassemble the original binary.

# Attack Execution

Using this, I was able to write a quick Node.js script that would brute force the characters. I’ve cleaned it up a bit and added comments for a bit of clarity.

# Analysis

Not being great at reverse engineering was for me a blessing, because otherwise I would have spent a lot of time and effort attempting to understand what the code was actually doing. Not being familiar with it gave me a different perspective, which allowed me to conceptualize a much easier solution to the challenge. I think this challenge was quite interesting, if not a bit misplaced given that it had very little to do with Web Exploitation.
