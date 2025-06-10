# 3.Write a program which accept file name from user and create new file named as Demo.txt and
# copy all contents from existing file into new file. Accept file name through command line
# arguments.
# Input : ABC.txt
# Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt


import sys
import os
      
def Copy(file_name):

    flag = os.path.exists(file_name)

    if flag == False:
        print("Invalid file name")
        exit()

    if flag == True:
        new_fobj = open("Demo.txt","w")
        old_fobj = open(file_name,"r")
        Buffer = old_fobj.read()
        new_fobj.write(Buffer)
        

def main():

    if(len(sys.argv) == 1):
        print("Use the given flags as : ")
        print("--h is used to display the help")
        print("--u is used to display the usage")

    elif (len(sys.argv) == 2):
        if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):
            print("This application is used to perform copy from source to destination of file")
        elif(sys.argv[1] == '--u' or sys.argv[1] == '--U'):
            print("Use the given script as ")
            print("Scriptname.py file_name")
            print("file_name :- the file that you want to make a copy")
        else:
            Copy(sys.argv[1])
            print("a new copy of file is sucessfully created as Demo.txt")
            
if __name__ == "__main__":
    main()