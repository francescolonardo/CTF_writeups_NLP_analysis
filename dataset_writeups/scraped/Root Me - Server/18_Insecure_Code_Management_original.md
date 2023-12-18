# Analysis
Insecure code management is when part of the code exposes sensitive information which shouldn’t be exposed to the world. Now it can happen in a lot of situation where the API keys/Passwords are hard-coded and it has been shared mistakenly by the developers. Here we will cover the part of Git version control feature and how attackers can gain sensitive information if it is exposed in .git directories of the webservers.

# Overview
This Challenge will present you with a web-App. There is not much information on the first page and it will ask you to enter login information.

# Analysis
A quick check will give you /.git. You can use wget or HTTrack to download the files and sub-directories.
 
Once downloaded, go to the .git directory and check the git log, that will give you information on the commits that has happened and gives you a history of the changes that has been done to the repository.
Now, we know changes has been made on the passwords and also that the password is in MD5 hash.

Let’s check the change status by using command : git status
The file config.php and index.php are the once that are deleted. Mostly when setting up a webApp, the DB passwords and the application passwords are stored in the config.php file. What we need to do now is to either restore this file or to checkout these files.

The next command I have used is : “git restore config.php” which gave me the required password.
The above hash can be checked against MD5 decryptor and we can get the relevant string.

# Attack Execution
The above approach is a manual one can be automated with plenty of tools out there. But the one I found pretty useful in such scenarios is “gittyleaks”.
To make use of this tool, all you require to do is to run it in the .git directory and it will fetch out any sensitive information it can find based on sensitive words and known conditions.
