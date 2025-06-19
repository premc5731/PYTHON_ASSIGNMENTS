# 1.Design automation script which accept directory name and display checksum of all files.
# Usage : DirectoryChecksum.py “Demo”
# Demo is name of directory.

import sys
import os
import hashlib


def CalculateChecksum(filename, blocksize = 1024):
    fobj = open(filename, 'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(blocksize)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(blocksize)

    fobj.close()

    return hobj.hexdigest()

def DirectoryChecksum(dirname):
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

    
    for FolderName, subFolderNames , FileNames in os.walk(dirname):
        for file in FileNames:
            filepath = os.path.join(FolderName,file)
            checksum = CalculateChecksum(filepath)
            print("%s checksum is %s" %(file, checksum))

def main():

    if(len(sys.argv) == 1):
        print("Use the given flags as : ")
        print("--h is used to display the help")
        print("--u is used to display the usage")

    elif (len(sys.argv) == 2):
        if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):
            print("This application is used to display checksum of  files")
        elif(sys.argv[1] == '--u' or sys.argv[1] == '--U'):
            print("Use the given script as ")
            print("Scriptname.py directoryname")
        elif (len(sys.argv) == 2):
            DirectoryChecksum(sys.argv[1])

    else:
            print("Use the given flags as : ")
            print("--h is used to display the help")
            print("--u is used to display the usage")

if __name__ == "__main__":
    main()