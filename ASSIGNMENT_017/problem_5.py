# 5. Schedule a job that runs every 5 minutes to write the current time to a file
# Marvellous.txt.

import time
import schedule
import os

def WriteFile(file_object):
    time_now = time.ctime()
    time_now = str(time_now)
    file_object.write(time_now + "\n")
    file_object.flush()

def ScheduleWork(file_name,min):
    flag = os.path.exists(file_name)

    if (flag == True):
        print("Filename already exists")
        print("please give unique name")
        exit()

    fobj = open(file_name,"w")

    schedule.every(min).minutes.do(lambda : WriteFile(fobj)) # change

    while(True):
        schedule.run_pending()
        time.sleep(1)

def main():
    print("Enter the file name : ", end="")
    fname = input()

    print("Enter the minutes : ",end="")
    min = int(input())

    ScheduleWork(fname,min)

if __name__ == "__main__":
    main()


# do() requires a reference to a function, not the result of calling a function.
# writeFile() → is called immediately

# do(...) receives whatever that function returns (often None)

# This breaks the scheduler

# lambda : WriteFile(fobj) 
# lly as 
# def temp_fun():
#     WriteFile(fobj)
    