Title: Calculat3 M3

A simple command injection challenge will be demonstrated in this walkthrough.

The site gives a calculator that you can click the buttons to input expression, then it will eval the expression and gives a result.
I provided random input in this calculator and intercepted the request with BurpSuite.

I got one parameter taking the values:
expression: 5 * 6 

Try to get the contents in directory, set the expression to ;ls. Submit it to get a list of file names in result, the flag is the one starts with ctf.
