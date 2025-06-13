# 4.Write a program which accept two file names from user and compare contents of both the
# files. If both the files contains same contents then display success otherwise display failure.
# Accept names of both the files from command line.
# Input : Demo.txt Hello.txt
# Compare contents of Demo.txt and Hello.txt


import sys
import os

def Compare(src_file,dst_file):

    src_flag = os.path.exists(src_file)
    dst_flag = os.path.exists(dst_file)

    if((src_flag == False) or (dst_flag == False)):
        print("Invalid file name")
        exit()
    
    src_fobj = open(src_file,"r")
    Buffer_src = src_fobj.read()

    dst_fobj = open(dst_file,"r")
    Buffer_dest = dst_fobj.read()

    if(Buffer_src == Buffer_dest):
        return True
    else:
        return False


def main():

    if(len(sys.argv) == 1):
        print("Use the given flags as : ")
        print("--h is used to display the help")
        print("--u is used to display the usage")

    elif (len(sys.argv) == 2):
        if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):
            print("This application is used to perform comparison between source file and destination file")
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
            print("Both files are same")
        else:
            print("Both files are different")

if __name__ == "__main__":
    main()