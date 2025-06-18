# 2. Schedule a task that displays the current date and time every minute using the
# datetime module.


import schedule
import time
import datetime

def Display():
    print(datetime.datetime.now())

def main():
    schedule.every(1).minutes.do(Display)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()