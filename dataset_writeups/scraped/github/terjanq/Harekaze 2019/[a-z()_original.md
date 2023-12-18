# /[a-z().]/

```js
if (code && code.length < 200 && !/[^a-z().]/.test(code)) {
    try {
      const result = vm.runInNewContext(code, {}, { timeout: 500 });
      if (result === 1337) {
        output = process.env.FLAG;
      } else {
        output = 'nope';
      }
    } catch (e) {
      output = 'nope';
    }
  } else {
    output = 'nope';
  }
```

We have to create a payload that when ran in the context will return 1337. My first solution was:
`escape.name.concat(eval.length).repeat(eval.name.concat(eval).repeat(eval.name.concat(eval.length).length).concat(escape.name).length).length` which is 141 characters long. It uses factorization of 1337 which is 7*191

Then I improved it to: 
`escape.name.concat(eval.length).repeat(escape(escape(escape(escape(escape(escape(escape(unescape))))))).length).length` which is 118 characters long

Then I just was poking around and the best I got for 7*191 was:
`console.profile.name.repeat(escape(escape(eval).sup().bold().link().link()).length).length` (90 characters)

However my best payload doesn't use the factorization:
`escape(escape(eval).repeat(escape.name.sup().length)).concat(eval.name.link()).length` and is only **85 characters long!**

One could possibly bruteforce the shortest solution but no fun there! :)

P.S  
splitline shared on discord a nice way to solve by joining 13 and 37 with the payload: `eval(escape(eval.name.fixed().length).concat(unescape(unescape).length))` (72)   

I improved my best payload to: `escape(escape().bold().repeat(escape(eval).length)).strike().length` and that is only 67 characters long!

The flag:
**HarekazeCTF{sorry_about_last_year's_js_challenge...}**