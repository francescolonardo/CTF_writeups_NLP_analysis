## Key-Lottery
> Solved by: Taz34

We have a simple website which asks for Keys and gives a set of rule.
“Keys should be sent as comma separated string of key guesses. Letters and digits only. No spaces.”
We also have an attachment server.py

![](https://i.imgur.com/ecj5VOC.png)

Now first we tried many diffrent chars like $,% etc, but we got an error

![](https://i.imgur.com/2O7YinW.png)

In the attachment file we see:
“/guess?keys=key0,key1,key2”
here we know that we need 3 keys.

After entering many different combination of inputs, we thought of using just comma as input.
At first we entered a single comma we got:

![](https://i.imgur.com/FejpM9s.png)

Now i though of giving 3 comma’s as input, as we have 3 keys:

![](https://i.imgur.com/IwAUcZ4.png)

And we got:

![](https://i.imgur.com/b4hLejF.png)

that looks like a character set.
So i tried using this a the input with 3 comma’s so as to complete the requirement:

![](https://i.imgur.com/UC4jCyo.png)

And here we have the flag:

![](https://i.imgur.com/0x1x0RQ.png)
