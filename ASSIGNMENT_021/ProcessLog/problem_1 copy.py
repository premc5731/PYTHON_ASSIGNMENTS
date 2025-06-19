# 1.Design automation script which display information of running processes as its name, PID,
# Username.
# Usage : ProcInfo.py

import psutil

def DisplayRunningProcesses():
    for proc in psutil.process_iter(['name','pid','username']):#less system calls
        print(proc.info) 

# we have 2 different approach which is better is 1st one explanation is in python class books or processkilling.py in automation/process automation in 
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['name','pid','username'])# more system calls almost 3 times more than first one because of 3 attributes
        print(info)


def main():
    DisplayRunningProcesses()

if __name__ == "__main__":
    main()