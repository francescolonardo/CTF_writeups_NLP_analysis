# Analysis
This challenge is talking about a vulnerability in eval function implementation in the PHP language. Basically, sometimes, we have established some firewalls like regular expression filtration, but unfortunately, it still can be bypassed. In this challenge, we will talk about how we bypass a regular-expression firewall.

# Overview
The challenge is as follows. There is a web-app that contains the eval function.

# Analysis
Eval function definition is as follows referring to PHP official site.
eval  Evaluate a string as PHP code

We need to know the target you want to achieve. Trust me, after several challenges I have done, it is always unsolvable if you do not know what to achieve. Even when you have the skills and tools. So getting information about the target is the thing you have to do in the first place.

This challenge also gives us the source code.
In the source code, we can see the process flow.
Here is the explanation.
Line 14. It checks whether the data we supplied does NOT contain A-Z, a-z, and  ` . It is actually a good firewall because it is really hard to do command injection without letters.
Line 1517. If it does not contain any of that, it will do the eval function. The eval executes the print function and execute any syntax we passed onto it. For example, we give input like 1+1, the result will be 2.


The challenge says we need to read the content of the .passwd file. As we can see, this is an os-related challenge which means we hope that we can execute several PHP functions that interact with OS.

# Attack Execution
Okay, the command we will be using is ready which is system(cat .passwd) or shell_exec(cat .passwd). Now the next question is how to bypass this command through the firewall that allows no letters.

# Analysis
This is where the experience comes to play. This is worth remembering. We can create characters from the XOR function, for example, ( XOR [ = S. Great! now we can create characters without letters.

# Attack Execution
Now our strategy is ready. We will construct system(cat .passwd) command from the combination of XOR symbols. Fingers crossed, this will execute as we hope.

# Analysis
The pain point is to build the command in XOR-ed symbols. We will use programming now. I create a program that converts a string into XOR-ed symbols.

Line 2. We establish the charset we are going to use. I do not use several characters such as  `  and    because it will raise a conflict with the firewall and the string separator (because the system is using    as the separator.......... or at least because I face error when doing it :) ).
Line 421. This is when the brute force happens. I loop all the requested string and convert them one by one.
Line 5. This is to set up the empty variable we will be using as our placeholder.
Line 720. Loop all the characters of the string because we have to encode them one by one. Because I find it really difficult to use the whole string xor-ed with another string, for example !@#$%&* XOR {}|[]\. It is difficult because it raises an error of miss XOR value. Because of that we will xor them one by one and use concatenation to combine all the xor values. This is why we need to loop these characters one by one.
Line 9. We set the flag to False. This value will be changed if we find the XOR combination.
Line 1018. We loop through every character in our symbols charset and try the combination one by one until we found the necessary combination.
Line 1214. We check if the XOR value of both symbols (in ASCII number, btw. That is what the ord function for) equals the character we want (in ASCII number as well).
Line 13. We format our output to be readable. If you notice, I put a leading dot. It is on purpose because the goal is to concatenation every character to be a string and concatenation in PHP is by using a dot.
Line 14. If the combination is found, then set the flag to True hence it does not need to continue the loop and can continue to the next character instead.
Line 1518. If the combination found, skip all the brute force processes and continue to the next character.
Line 1920. Just in case the combination is not found, just put the original value into the placeholder.
Line 21. We print the output.
Okay, that is the code. Now we will try our first exploit. Our target expression to be executed is print system(id);. The print part has been handled by the challenge, we need to supply the system(id). We execute and this is what I get.

# Attack Execution
system('id') = ('('^'[').('$'^']').('('^'[').(')'^']').('%'^'@').('-'^'@').'('.('['^'|').(')'^'@').('$'^'@').('['^'|').')'
Do you see it? We are concatenating every character produced by XOR-ed symbols. Now we send it to the challenge page. Yay, it works!

# Analysis
HAHAHAHAHAH it does work though we pass some string and it is executed, but, that is not what we want, is it? We want the system(id) command is actually parsed and executed. This is where another experience comes to play. There are several ways to call a function in PHP.

We want to call the PHP legacy function. That is why we need to try the third one.

We are about to call system(command). In the third form, it looks like (system)(command). Now we break down again.

# Attack Execution
We can easily pass the parentheses because it is not letters
We need to convert the system string into symbols.
We also need to convert the command cat .passwd into symbols.
And we input it to our program before and it resulted like below.