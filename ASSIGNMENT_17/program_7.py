# 7. Schedule a function that performs file backup every hour and writes a log entry
# into backup_log.txt.


import time
import schedule
import os
import datetime

def LogEntry(file_object):
    time_now = datetime.datetime.now()
    time_now = str(time_now)
    file_object.write(time_now + "\n")
    file_object.flush()

def BackupLog(file_name,hr):
    flag = os.path.exists(file_name)

    if (flag == True):
        print("Filename already exists")
        print("please give unique name")
        exit()

    fobj = open(file_name,"w")

    schedule.every(hr).hour.do(lambda : LogEntry(fobj)) # change

    while(True):
        schedule.run_pending()
        time.sleep(1)

def main():
    print("Enter the file name : ", end="")
    fname = input()

    print("Enter the hours : ",end="")
    hr = int(input())

    BackupLog(fname,hr)

if __name__ == "__main__":
    main()


# do() requires a reference to a function, not the result of calling a function.
# writeFile() → is called immediately

# do(...) receives whatever that function returns (often None)

# This breaks the scheduler

# lambda : Log(fobj) 
# lly as 
# def temp_fun():
#     Log(fobj)
    