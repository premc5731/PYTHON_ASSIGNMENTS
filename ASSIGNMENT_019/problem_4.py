# 4. Design automation script which accept two directory names and one file extension. Copy all
# files with the specified extension from first directory into second directory. Second directory
# should be created at run time.
# Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files with extension .exe from Demo to Temp.
import sys
import os

def DirectoryCopyExtension(old_dir,new_dir,ext):
    flag = os.path.isabs(old_dir)

    if(flag == False):
        old_dir = os.path.abspath(old_dir)

    flag = os.path.exists(old_dir) 

    if(flag == False):
        print("Invalid directory name ")
        exit()
    flag = os.path.isdir(old_dir)

    if(flag == False):
        print("given name is not directory")
        exit()
    
    old_parent_dir = os.path.dirname(old_dir)

    new_dir_path = os.path.join(old_parent_dir,new_dir)

    flag = os.path.exists(new_dir_path)

    if(flag == False):
        os.mkdir(new_dir_path)
    else:
        print("new directory already exists")
        print("Please provide a unique directory name")
        exit()
    for FolderName, SubFolderNames, FileNames in os.walk(old_dir):
        for file in FileNames:
            fname, fext = os.path.splitext(file)

            if(fext == ext):
                old_file_path = os.path.join(FolderName,file)
                old_fobj = open(old_file_path,"r")
                old_buffer = old_fobj.read()

                new_file_path = os.path.join(new_dir_path,file)
                new_fobj = open(new_file_path,"w")
                new_fobj.write(old_buffer)

def main():

    if(len(sys.argv) == 1):
        print("Use the given flags as : ")
        print("--h is used to display the help")
        print("--u is used to display the usage")

    elif(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to copy specified extension files from one directory to another directory  ")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):    
            print("Use the given script as ")
            print("Scriptname.py old_dir new_dir extension")
        else:
            print("Use the given flags as : ")
            print("--h is used to display the help")
            print("--u is used to display the usage")
    elif(len(sys.argv) == 4):
        DirectoryCopyExtension(sys.argv[1],sys.argv[2],sys.argv[3])
        print("Copying of files is done")

if __name__ == "__main__":
    main()
    