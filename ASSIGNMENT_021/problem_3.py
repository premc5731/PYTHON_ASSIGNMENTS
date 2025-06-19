# 3. Design automation script which accept directory name from user and create log file in that
# directory which contains information of running processes as its name, PID, Username.
# Usage : ProcInfoLog.py Demo
# Demo is name of Directory.



import psutil
import sys
import time
import os


def CreateLog(Data):
    dirname = sys.argv[1]
    flag = os.path.isabs(dirname)

    if flag == False:
        dirname = os.path.abspath(dirname)

    flag = os.path.exists(dirname)

    if flag == False:
        print("Invalid directory name")
        exit()

    flag = os.path.isdir(dirname)

    if flag == False:
        print("Given name is not directory")
        exit()

    timestamp = time.ctime()
    filename = "Running_Porcesses_Log %s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")
    filename = filename.replace("__","_")

    filename = os.path.join(dirname,filename)

    fobj = open(filename, "w")

    border = "-"*80
    fobj.write(border+"\n")
    fobj.write("This is a log file of delete_duplicate_files automation script\n")
    fobj.write(border+"\n")

    for value in Data:
        fobj.write(value)
        fobj.write("\n")

    
    fobj.write(border+"\n")
    fobj.write("Total running processes are : %s \n"%(len(Data)))
    fobj.write("This file is created at\n"+timestamp+"\n")
    fobj.write(border+"\n")

    fobj.close()


def DisplayRunningProcesses():
    info_list = []
    for proc in psutil.process_iter(['name','pid','username']):#less system calls
        info_list.append(str(proc.info))

    CreateLog(info_list)
         

def main():
    DisplayRunningProcesses()

if __name__ == "__main__":
    main()