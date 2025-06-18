# 1.Design automation script which accept directory name and file extension from user. Display all
# files with that extension.
# Usage : DirectoryFileSearch.py “Demo” “.txt”


import sys
import os

def DirectoryFileSearch(dirname,ext):
    flag = os.path.isabs(dirname)

    print("__file__",__file__)

    if(flag == False):
        dirname = os.path.abspath(dirname)

    flag = os.path.exists(dirname)

    if( flag == False):
        print("Invalid directory name")
        exit()
    flag = os.path.isdir(dirname)

    if(flag == False):
        print("given name is not directory")
        exit()

    for FolderName, subFolderNames, FileNames in os.walk(dirname):
        for file in FileNames:
            name,fext = os.path.splitext(file)
            if(fext == ext):
                print(file)
   
def main():

    if(len(sys.argv) == 1):
        print("Use the given flags as : ")
        print("--h is used to display the help")
        print("--u is used to display the usage")

    elif (len(sys.argv) == 2):
        if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):
            print("This application is used to display the files with the given extension ")
        elif(sys.argv[1] == '--u' or sys.argv[1] == '--U'):
            print("Use the given script as ")
            print("Scriptname.py src_path extension")
        else:
            print("Use the given flags as : ")
            print("--h is used to display the help")
            print("--u is used to display the usage")
    
    elif (len(sys.argv) == 3):
        DirectoryFileSearch(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
    main()