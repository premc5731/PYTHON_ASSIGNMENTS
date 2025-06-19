# 4. Design automation script which accept directory name and delete all duplicate files from that
# directory. Write names of duplicate files from that directory into log file named as Log.txt.
# Log.txt file should be created into current directory. Display execution time required for the
# script.
# Usage : DirectoryDusplicateRemoval.py “Demo”
# Demo is name of directory.


import sys
import os
import hashlib
import time


def CreateLog(Data):

    timestamp = time.ctime()
    filename = "Delete_Duplicate_Files_Log %s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")
    filename = filename.replace("__","_")

    fobj = open(filename, "w")

    border = "-"*80
    fobj.write(border+"\n")
    fobj.write("This is a log file of delete_duplicate_files automation script\n")
    fobj.write(border+"\n")

    for value in Data:
        fobj.write(value)
        fobj.write("\n")

    
    fobj.write(border+"\n")
    fobj.write("Total deleted files : %s \n"%(len(Data)))
    fobj.write("This file is created at\n"+timestamp+"\n")
    fobj.write(border+"\n")

    fobj.close()

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

    Duplicate = {}
    dup_files = []
    
    for FolderName, subFolderNames , FileNames in os.walk(dirname):
        for file in FileNames:
            filepath = os.path.join(FolderName,file)
            checksum = CalculateChecksum(filepath)

            if checksum in Duplicate:
                Duplicate[checksum].append(filepath)
                if (len(Duplicate[checksum]) > 1):
                    dup_files.append(filepath)
                    os.remove(filepath)

            else:
                Duplicate[checksum] = [filepath]

    CreateLog(dup_files)
            

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
            start_time = time.time()
            DirectoryChecksum(sys.argv[1])
            end_time = time.time()
            print("Execution time required : ",(end_time - start_time))

    else:
            print("Use the given flags as : ")
            print("--h is used to display the help")
            print("--u is used to display the usage")

if __name__ == "__main__":
    main()