# 2. Write a program to read and display the contents of a file data.txt.


import sys
import os
        
def Display(file_name):

    flag = os.path.exists(file_name)

    if(flag == False):
        print("Invalid file name")
        exit()
    
    fobj = open(file_name,"r")
    Buffer = fobj.read()
    print("File content : ")
    print(Buffer)

def main():

    if(len(sys.argv) == 1):
        print("Use the given flags as : ")
        print("--h is used to display the help")
        print("--u is used to display the usage")

    elif (len(sys.argv) == 2):
        if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):
            print("This application is used to display the content of a file")
        elif(sys.argv[1] == '--u' or sys.argv[1] == '--U'):
            print("Use the given script as ")
            print("Scriptname.py file_name")
        else:
            Display(sys.argv[1])
    
if __name__ == "__main__":
    main()