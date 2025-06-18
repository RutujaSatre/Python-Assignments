# Write a script that simulates checking for email updates every 10 seconds. (Use a print statement like "Checkimg mail..." instead of real email logic.

import time
import schedule

def Chk_email():
    timestamp = time.ctime()
    print("Checking mail..."+timestamp)

def main():
    schedule.every(10).seconds.do(Chk_email)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()