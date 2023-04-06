Title: Live Art

Live Art is one of my favourite challenges from picoCTF 2022. Its a React website that contains a hidden flaw: a XSS vulnerability. Normally React protects you from most XSS problems, so something must have gone horribly wrong.

The Problem
Exploring the website doesnt reveal too much. Its pretty clear that the /link-submission page is intended for you to submit a link that will be clicked-on by a victim (In this case the victim is a headless browser, but thats largely irrelevant here).

Looking closer at what happens when you submit a link (this is in the code directory under server), we learn that the flag we are looking for is stored in the browsers local storage for the live-art website, under the key "username". All we have to do is figure out how to leak that information from a client that clicks on our link.

Sources and Sinks
We can provide the victim a link. That means we are fundamentally in control of one thing: a URL. We start out wondering if theres anything on the website where the url has a direct impact on the rendered HTML (or javascript). It doesnt take long for us to find the /error route, which is backed by this ErrorPage component.

In particular the useHashParams function stands out to us. Whatever that function returns influences a link and the content of an h3 block. So, what does useHashParams do?

Aha! This is interesting. Theres some state being stored inside React, and that state is an object constructed by iterating through the hash parameters and storing the key/value pairs. This means that navigating to a url like /error#returnTo=/foo&error=Error%20Message will give us a page containing an <h3> Error Message and a link to the page /foo (try it!). However, React is very good about escaping these inputs, so its not directly vulnerable to XSS. We can inject a "javascript:" link, but we cant actually get the headless browser to click it, so its not directly helpful to us.

We do notice that there is a suspicious loop, and we initially wondered if it might be vulnerable to a prototype pollution vulnerability, but it didnt seem like it after some testing.

This ErrorPage component was the only obvious source for us to inject content in the URL and have it end up influencing the DOM / javascript. We also looked into the live-art broadcast feature, but the incoming data from peers was only used to influence an <img> src data, so it didnt seem possible to inject javascript that way.

We take a break from looking at sources and try to find sinks - these are places where javascript variables might end up affecting the dom. In particular were interested in being able to directly inject html elements (like <script>), or possibly some element attributes (onload, onerror and the like). One of the most common ways this might happen is the use of the ... spread operator, as that could unintentionally include unintended state.

Lets grep for it.
Immediately the second line jumps out at us. Heres an img tag where the dimension object is directly used as attributes on the element itself. What is this dimension object and what values does it have?

Hmmm... Its a reducer with an initial value of baseResolution and some logic adjusting width/height. In general it seems that it only ever works with the width and height properties, so its not obvious how we could inject a more interesting attribute, like the classic onerror attribute often used on img tags for XSS.

Development Environment
The javascript on the live website has been bundled/minimized and doesnt lend itself to debugging. Fortunately we have the source code, but not really any instructions on how to use it. Since were only interested in the client code right now, lets try and host that code ourselves, hopefully with source maps for ease of debugging. To do that, well whip up a Dockerfile, based largely on the one they gave us for the noted challenge.

The Dockerfile contains some unnecessary components (we need puppeteer for the server project, but not client). In any case, its good enough for now. Build it and run it.

This will give us a development server running on port 3000. Loading it up, we are again greeted with the live-art website, but this time dev-tools has working source maps, and we can even use breakpoints.

The Error Message
At this point were a bit out of ideas. We have a source (the ErrorPage component), and a sink (the Viewer component), but individually they appear benign. We load up the development server and start poking around for something we missed.

After poking around for a bit, we stumble across the Drawing component. This component appears to reference both an ErrorPage component and a Viewer component. Its used if you go to a valid /drawing route, such as /drawing/abcd. The logic seems to be that if the window is too small then the error component is used, and if the windows is large enough then the viewer component is used. The use of these two components together on the same page is setting off alarm bells in our heads, but how can we exploit it?

One thing we notice is that if were on the /drawing/abcd page and we resize the window small enough, the javascript console starts spitting out error messages. This is something we didnt see on the release version of the website, so it must be something to do with the fact that were now using React in developer mode. At this point were pretty sure weve found the vulnerability. But what is it?

Injecting an attribute
Since we know the ErrorPage component will read from hash parameters, lets load up the drawing route in a window that is really small, so that it starts with an ErrorPage component. Navigating to /drawing/abcd#error=abcd with the window small doesnt initially seem to do anything. It doesnt even override the displayed error message. However, if we now resize the window so that its large, something interesting happens.

In addition to the error message in the javascript console, inspecting the DOM now reveals this element.
<img error="abcd">

Aha! That state that the ErrorPage component uses must be getting re-used in the wrong context. It replaces the dimensions variable in the Viewer component, allowing us to inject attributes on the <img> tag.

Lets try that again, but this time with /drawing/abcd#src=1&onerror=alert(1). Remember, the window has to start out small and then be resized larger.

Unfortunately, that doesnt work:
```
Warning: Invalid event handler property `onerror`. Did you mean `onError`?
```

React is pretty specific about its handlers. In general it expects you to provide things the React way rather than using raw javascript. It even requires the onError attribute to be a function and not a string, so simply adjusting the case in our URL doesnt help. We start banging our heads against the wall, since were so close to cracking this thing.

A solution
Desperately researching React XSS vulnerabilities, we come across this article from a 2021 CTF writeup. It reveals the secret: if your object has an "is" property, then react will treat the whole thing as a WebComponent and pass the attributes straight through. Lets try it out: /drawing/abcd#src=1&onerror=alert(1)&is (remember, start with the window small and then resize it so that its larger).

Success - we are greeted with an alert popup! We can now execute javascript on the page. All thats left to do is weaponize this. Well load up the drawing route in a small iframe with our XSS payload in the hash parameters. Well then resize the iframe to trigger the vulnerability. All our payload has to do is read from localstorage and send it to our server.

We can now host our payload with a simple http server using python3 -m http.server and then make it publicly accessible using ngrok http 8000. This will give us an http/https server on a .ngrok.io subdomain that we can put into the link-submission form. (I tried using other ports and they were blocked, so I believe the challenge only supports connecting to servers on either port 80 or 443).

As we can see here, the XSS worked, and about 1 second after the request for our xss payload we get another request containing the flag!
