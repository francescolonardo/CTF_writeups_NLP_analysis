## Amidst Us
> Solved by : thewhiteh4t, Starry-Lord, Taz34, Avantika, Legend

![](https://i.imgur.com/r7mbpDi.png)

The downloadable files gives us a few clues in the files in requirements.txt and util.py:

* It’s a python environment
* It uses a vulnerable version of the python Pillow library

![](https://i.imgur.com/oeEjFBA.png)

https://github.com/python-pillow/Pillow/pull/5923

link: [python-pillow/Pillow#5923](https://github.com/python-pillow/Pillow/pull/5923)

This exchange provided some great insights on how to trigger SSRF

In util.py we find eval is being used on the data provided in the POST request, which allows us to upload a random image with background rgb parameters.

After a couple trial and errors we managed to grab the flag.txt and send it to our webhook by replacing one of the RGB values of “background”:

![](https://i.imgur.com/8kemcYF.png)

```
HTB{i_slept_my_way_to_rce}
```
