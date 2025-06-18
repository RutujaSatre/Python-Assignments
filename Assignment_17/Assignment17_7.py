# Schedule a function that perform file backup every hour and writes a log entry into backup_log.txt .


import schedule
import time

def Display():
    timestamp = time.ctime()

    file = open('backup_log','w')
    file.write("This is a Backup File")

    file.write("Backup Completed at : "+timestamp)
    

def main():
    schedule.every(1).hour.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()