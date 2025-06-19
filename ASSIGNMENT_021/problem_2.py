# 2.Design automation script which accept process name and display information of that process if
# it is running.
# Usage : ProcInfo.py Notepad

import sys
import psutil

def DisplayInfo(proc_name):
     
     for proc in psutil.process_iter(['name','pid','username','status']):
          if(proc.info['name'] == proc_name):
               print(proc.info)
          

def main():

    if(len(sys.argv) == 1):
        print("Use the given flags as : ")
        print("--h is used to display the help")
        print("--u is used to display the usage")

    elif (len(sys.argv) == 2):
        if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):
            print("This application is used to display information of running process")
        elif(sys.argv[1] == '--u' or sys.argv[1] == '--U'):
            print("Use the given script as ")
            print("Scriptname.py processname")
        elif (len(sys.argv) == 2):
            DisplayInfo(sys.argv[1])

    else:
            print("Use the given flags as : ")
            print("--h is used to display the help")
            print("--u is used to display the usage")

if __name__ == "__main__":
    main()