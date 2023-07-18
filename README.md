# Withings-Garmin-MFA

Since there was no single project that downloaded data from Withings, sent that data to Garmin Connect, ***AND*** handled Garmins MFA, I decided to merge multiple projects together to get it working fully automated end to end!

Note that this is very clunky and isn't optimized/still has lingering code from both repos that isn't being used, but maybe eventually (if I can find extra time), that'll be taken care of :)

Best best is to use this with docker (similar to withings-sync) as I've only tested with this method:

`docker build -t withings-sync-mfa`
```
docker run --name withings -v $HOME:/root --interactive --tty withings-sync-mfa --garmin-username='YOUR_USERNAME' --garmin-password='YOUR_PASSWORD' --fromdate='2023-07-17' --garmin-mfa True --email-login 'YOUR_ACTUAL_LOGIN_TO_YOUR_EMAIL' --email-password 'YOUR_EMAILS_PASSWORD' --email-server "imap.gmail.com"
```

**NOTE:** If you want MFA to work, this requires: 

- SMS MFA must be disabled/Email MFA must be default
- You to be able to login to your email server to retrieve the MFA code.
    - I use gmail, and to login to the imap server, gmail requires an application password. This can be obtained from:
        - Google Account Settings > Security > 2-Step Verification (turned on) > App Passwords

# Credits
The following projects are referenced/used in this repository:

- https://github.com/jaroslawhartman/withings-sync
- https://github.com/cam-rod/python-garminconnect/tree/mfa-login