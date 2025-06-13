# 2. Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion.
# Usage : DirectoryRename.py “Demo” “.txt” “.doc”
# Demo is name of directory and .txt is the extension that we want to search and rename
# with .doc.
# After execution this script each .txt file gets renamed as .doc.


import sys
import os

def DirectoryFileSearch(dirname,old_ext,new_ext):
    flag = os.path.isabs(dirname)

    # print("__file__",__file__)

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
            if(fext == old_ext):
                # print("foldrname",FolderName)
                old_file_path = os.path.join(FolderName,file)
                new_filename = name + new_ext
                new_file_path = os.path.join(FolderName,new_filename)
                os.rename(old_file_path,new_file_path)
   
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
            print("Scriptname.py dirname old_extension new_extension")
        else:
            print("Use the given flags as : ")
            print("--h is used to display the help")
            print("--u is used to display the usage")
    
    elif (len(sys.argv) == 4):
        DirectoryFileSearch(sys.argv[1],sys.argv[2],sys.argv[3])


if __name__ == "__main__":
    main()