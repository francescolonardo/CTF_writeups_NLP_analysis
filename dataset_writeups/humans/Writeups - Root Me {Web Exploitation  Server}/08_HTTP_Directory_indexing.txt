# Overview
This challenge provides you with the supposed directory for the password in the source code of the page.
However, if you visit the page, there’s nothing there.

# Analysis
If you go back and pay closer attention to the directory they gave you, it turns out to be a subdirectory, with the root directory being /admin. Navigate to /admin and you’ll be able to see more files.

# Attack Execution
The password should be in /admin/backup/admin.txt.
