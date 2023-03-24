#overview
Only local users will be able to access the page

---

Dear colleagues,

We’re now managing connections to the intranet using private IP addresses, so it’s no longer necessary to login with a username / password when you are already connected to the internal company network.

Regards,

The network admin

---

#analysis
In this challenge we will study the bypassing of IP filtering by a well-known technique of HTTP headers injection. Some of these headers allow you to specify that the client’s IP address is different from the source IP address in the packet received by the server. These headers are particularly useful when the connections go through a load-balancer or a proxy. However we can also use these headers to indicate the IP we want. 

#attack_execution
So we will try request with CURL and this HTTP header!

curl 'http://challenge01.root-me.org/web-serveur/ch68/' --header 'X-Forwarded-For: 192.168.1.1'
And we get :

Well done validation password is : <strong>FLAGFLAGFLAGFLAGFLAGFLAG</strong>
