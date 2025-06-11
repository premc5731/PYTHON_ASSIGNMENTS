# 6. Write a script that schedules multiple tasks: one to print "Lunch Time!" at 1 PM,
# and another to print "Wrap up work" at 6 PM.

import schedule
import time

def DisplayLunch():
    print("Lunch Time!")

def DisplayWrap():
    print("Wrap up work")

def Script():

    schedule.every().day.at("13:00").do(DisplayLunch)
    schedule.every().day.at("18:00").do(DisplayWrap)

    while(True):
        schedule.run_pending()
        time.sleep(1)

def main():
    Script()

if __name__ == "__main__":
    main()