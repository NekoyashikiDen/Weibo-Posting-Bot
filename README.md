# Weibo-Posting-Bot
worked in python 3

i wrote this program for testing robots on weibo.
unfortunately weibo had closed some important api for posting and only left statuses/share, so i had to try a new way.

instructions:
1. sign up a weibo application account and get the app_key and app_secret
2. install sinaweibopy3 with “pip install sinaweibopy3”
3. set a callback url for the account as in the code file
4. set a security domain for the account, and any website under it to "passport_url" in the code file (this is tricky but weibo asked for it)
5. run the code, copy the link it returns and access it, then choose "authorizing" and copy the code part in the url
6. paste the code back to the program, it will start posting in a moment

the post content in the file is in stR and fullpic, the program would add your passport_url to stR automatically.
the pic posted should be under 5MB or may cause a fail.
