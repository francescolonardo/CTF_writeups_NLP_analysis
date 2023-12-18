Title: Bithug

BigHug was my favorite web challenge on the CTF. The way this challenge was presented was very well thought out and gave you just enough hints such that you were never led to a point where you had no direction to go. All you needed to do was to put all the different things together and figure out how to execute the exploit.

How it Works
BitHug is a web app listening on port 1823 that lets you do basic version control with Git. To do this, it uses the Git CLI to perform operations on repositories. The goal of this challenge is to get access to a Git repository that you do not own, and to prove that you can do this, you have to clone a (normally inaccessible) repository under the name ```_/{your username}```, with the flag in it.

Theres a lot of things that you can explore with this challenge, here Ill outline the important ones for our final exploit.

User type admin
When starting on a CTF challenge, the first thing I do is to look for a destination. Getting access to a repository that you dont own should be impossible because the permission controls for repositories are very simple and on first glance, has no obvious problems. However, there is a caveat in that if you make requests from a loopback IP address (```127.0.0.1```, ```::1``` or ```::ffff:127.0.0.1```), you will be given essentially godmode powers so you can access any repository. Its clear here that our goal is to somehow make requests from a loopback IP address, hinting at some kind of server-side resource forgery (SSRF) exploit.

git-receive-pack
```git-receive-pack``` is the endpoint that is used by Git to perform remote operations on a repository. In other words, when you ```git push```, the CLI converts your changes into a pack (```application/x-git-receive-pack-request```) and POSTs it to the server.

Webhooks
BigHug has functionality that lets you specify POST webhooks that will be triggered when you make changes to a repository (more formally, it does this when it executed as git-receive-pack command). You are able to provide it with a URL, content that you would like to POST to that URL as well as the Content-Type of the content. The content that you provide is then put through a simple templating engine that allows you to inject certain attributes of the commit into your webhook. Ill go more in depth on this below where I explain how the exploit works.

Access Control
Repositories can be accessed by the creator of the repository or a list of people as defined in the access.conf file of the refs/meta/config commit of the repository. This hints us toward us needing to somehow modify this file as part of our exploit.

The Webhook Exploit
The main thing that we will be exploiting is how webhooks are processed and sent. Webhooks are a SSRF vector, and in theory we can make a webhook that POSTs a git-receive-pack that adds our user to the access.conf file. However, this exploit wont work since the server sanitizes our webhooks and only allows you to make webhooks that request to port 80. It does this by parsing our URL using the URL class.

However, when actually executing the webhook, there is an exploit that allows us to bypass this.

So it will replace all {{attr}} in a string with options[attr].

The important part of this is const url = formatString(webhook.url, options);. This is a template injection vulnerability that allows us to enter a URL like http://{{ref}}.com, and then inject a ref that points to 127.0.0.1:1823/_/admin.git/git-receive-pack?a to bypass the port check since it only happens when the webhook is created.

Surprisingly enough, Node.js URL will actually accept http://{{ref}}.com as valid and parses it accordingly.

The final url would be http://127.0.0.1:1823/_/admin.git/git-receive-pack?a.com, with the webserver ignoring the query string.

Now all we need to do is to somehow inject a string into the ref of a git-receive-pack. We can look at how the ref is parsed in the receivePackPost function.

This parsing is just basic string splitting so it should be easily exploitable.

The Execution
Given all of this the full exploit should be the following:

1. Create a webhook with URL http://{{ref}}.com, Content-Type: application/x-git-receive-pack-request and the content of a git-receive-pack that commits our user account to the access.conf of the refs/meta/config.

2. Trigger the webhook with a commit ref being 127.0.0.1:1823/_/admin.git/git-receive-pack?a.

The hard part of this challenge is figuring out how to properly execute this exploit. There is very little documentation on the git-receive-pack format and it seems nontrivial to figure out what the format actually is.

Instead of figuring out how the format works, we can instead simply use the Git CLI to try making commits and reading the requests that it makes. Most people would go straight to Wireshark for this purpose, but for the sake of simplicity I instead chose to modify the source code of the app and simply log out the hex of the request body directly.

After doing this, we can make any commit to the repository and push it. Then we can take the raw body and replace the ref with our payload. I chose to make a very long branch name (e.g. aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa) to make it easier to edit the raw data using a hex editor.

Next, we can follow the instructions on the website and use the same method discussed above to generate the git-receive-pack that includes a commit to access.conf to add our own user.

Now that we have our payloads in place, we can make a short script to automate the exploit. We first make the webhook with the template injection URL and payload for adding us to the repository and then we trigger that webhook with the ref injection.

Now, we can just visit _/admin on the web interface and you should be able to read the flag.

Conclusion
This was a great challenge by all measures. It did not require any guessing (unlike a lot of the other challenges), and it taught me a lot about how Git works in the background. The execution wasnt anywhere near as hard as it looked initially. For me, this felt like a well designed challenge that successfully challenges many of the assumptions that we make with the expected behavior of a programming language and its standard library.