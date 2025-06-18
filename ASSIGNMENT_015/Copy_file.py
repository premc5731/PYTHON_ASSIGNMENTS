
import sys
import os
import shutil

def Copy(src_file,dst_file):

    src_flag = os.path.exists(src_file)
    dst_flag = os.path.exists(dst_file)

    if((src_flag == False) or (dst_flag == False)):
        print("Invalid file name")
        exit()
    
    shutil.copyfile(src_file,dst_file)
        
def main():

    if(len(sys.argv) == 1):
        print("Use the given flags as : ")
        print("--h is used to display the help")
        print("--u is used to display the usage")

    elif (len(sys.argv) == 2):
        if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):
            print("This application is used to perform copy from source file to destination file")
        elif(sys.argv[1] == '--u' or sys.argv[1] == '--U'):
            print("Use the given script as ")
            print("Scriptname.py src_path dest_path")
        else:
            print("Use the given flags as : ")
            print("--h is used to display the help")
            print("--u is used to display the usage")
    
    elif (len(sys.argv) == 3):
        Copy(sys.argv[1],sys.argv[2])
        print("Copying of file is done")

if __name__ == "__main__":
    main()