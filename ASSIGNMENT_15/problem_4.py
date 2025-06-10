# 4.Write a program which accept two file names from user and compare contents of both the
# files. If both the files contains same contents then display success otherwise display failure.
# Accept names of both the files from command line.
# Input : Demo.txt Hello.txt
# Compare contents of Demo.txt and Hello.txt


import sys
import os
        
def Compare(src_file, dest_file):
    ret_flag = False

    src_flag = os.path.exists(src_file)
    dest_flag = os.path.exists(dest_file)

    if((src_flag == False) or (dest_flag == False)):
        print("Invalid file name")
        exit()
    src_fobj = open(src_file,"r")
    src_Buffer = src_fobj.read()

    dest_fobj = open(dest_file,"r")
    dest_Buffer = dest_fobj.read()

    if src_Buffer == dest_Buffer:
        ret_flag = True
    else:
        ret_flag = False

    return ret_flag


def main():

    if(len(sys.argv) == 1):
        print("Use the given flags as : ")
        print("--h is used to display the help")
        print("--u is used to display the usage")

    elif (len(sys.argv) == 2):
        if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):
            print("This application is used to compare source file and destination file content")
        elif(sys.argv[1] == '--u' or sys.argv[1] == '--U'):
            print("Use the given script as ")
            print("Scriptname.py src_path dest_path")
        else:
            print("Use the given flags as : ")
            print("--h is used to display the help")
            print("--u is used to display the usage")
    
    elif (len(sys.argv) == 3):
        ret = Compare(sys.argv[1],sys.argv[2])
        if ret == True:
            print("Both file contains same content")
            print("Success")

        else:
            print("Both file contains different content")
            print("Failure")

if __name__ == "__main__":
    main()