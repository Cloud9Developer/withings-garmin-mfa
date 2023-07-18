from imap_tools import MailBox, AND, MailMessageFlags
import os
import re
import time

# Server is the address of the IMAP server
class ReadEmail:
    def getMFAcodeFromEmail():
        timeout = 300
        sleep = 5        

        server = os.environ["EMAIL_SERVER"]
        user = os.environ["EMAIL_EMAIL"]
        password = os.environ["EMAIL_PASSWORD"]

        # print(f"Server: {server} ; User: {user} ; Password: {password}")

        mb = MailBox(server).login(user, password)

        while True:
            time.sleep(sleep)
            if timeout == 0:
                print("ERR: Timeout limit reached trying to get MFA code..")
                return "NA"
            print(f"Scanning Messages.. {timeout} seconds until timeout")

            if timeout % 20 == 0:
                mb = MailBox(server).login(user, password)

            messages = mb.fetch(criteria=AND(seen=False, from_="alerts@notifications.garmin.com"),
                                bulk=True)

            for msg in messages:
                # Print form and subject
                print(msg.from_, ': ', msg.subject)
                # Print the plain text (if there is one)
                mfa_code = re.findall(r"\d{6}</strong>",msg.html)[0].split('<')[0]
                print(mfa_code)
                if mfa_code is not None:
                    return mfa_code.strip()
                break
            timeout -= sleep

# ReadEmail.getMFAcodeFromEmail()