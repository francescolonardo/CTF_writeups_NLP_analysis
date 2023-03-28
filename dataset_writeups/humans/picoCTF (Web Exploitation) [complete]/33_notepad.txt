Title: notepad

We visit the website and get a note-taking application. After posting a note, the note contents get saved to a file on the server and we can visit it and view the note.

For example, if we post test, we are redirected to a URL such as https://notepad.mars.picoctf.net/static/test-gDpEQjbSwSQ.html which contains our note: test. The URL is composed of the first 128 characters of our note, concatenated to a hyphen and then a random string. The file is saved as an HTML file in the static folder.

Reviewing the code, we know that we can affect the address to which the note is written to, since we control the content.

For example, if we would enter a path that contains a slash into the first 128 characters of the note, we would be able to change the directory to which the file is written to. However, the application checks for this earlier.

Notice though that content[:128] isn't used as-is for the path - it's first passed to werkzeug.urls.url_fix.

Fortunately for us, the first step of the function is to switch to text processing and to convert backslashes (which are invalid in URLs anyways) to slashes. So, we can use this to bypass the slash check and write to a different directory.

Where should we write to? Well, one interesting place to write a file to is templates/errors. We can then use the following logic to include the file we've written to as part of a template.

Let's try the flow once manually and then automate it.

We will paste the following note:
```
..\templates\errors\aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcdefg
This is a test
```

We use the first 128 characters to control where the note will be written to. We want it to be written to /templates/errors, and we fill up the rest of the 128 characters with fillers so that our "payload" (currently This is a test following directly after) doesn't get mixed in with the file name.

After posting this note, we get redirected to https://notepad.mars.picoctf.net/templates/errors/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcdefg-fY1TxE2Zt-M.html. So we take the HTML file name, and visit it.

Now for some automation we can write a script.
This basically does the same thing, with a few added features:

Extracting just the payload from the HTML file using start and end markers.
Allowing us to provide parameters to the page we are visiting (we'll use that soon).
Let's try it out.

Since our payload gets interpreted as a Flask template, we can inject template syntax.
We'll use it to try and execute the known Python Sandbox escape to achieve RCE. For the first phase, we need to access the __class__ of some Python object.

And since underscore is blocked, the parameters come in. Instead of using request.__class__, we use request[request.args.param1] and send param1=__class__.

Finally, we just need to send 
```
{{request[request.args.p1][request.args.p2][11][request.args.p3]()[183]()[request.args.p4][request.args.p5]['open']('flag-c8f5526c-4122-4578-96de-d7dd27193798.txt').read()}}```
in order to read the flag.
