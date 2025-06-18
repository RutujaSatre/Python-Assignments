# Schedule a job that runs every 5 minutes to write the current time to a file Marvellous.txt.

import schedule
import time

def CurrentTime():
    timestamp = time.ctime()
    file = open('Marvellous.txt','w')
    file.write("Current time is : "+timestamp+"\n")


def main():
    schedule.every(5).minutes.do(CurrentTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()