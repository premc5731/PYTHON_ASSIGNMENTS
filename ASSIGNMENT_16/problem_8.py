# 8. Write a script to remove all blank lines from a file. Save the cleaned output to a
# new file.


import sys
import os

def RemoveBlankLines(file_name):

    flag = os.path.exists(file_name)

    if(flag == False):
        print("Invalid input")
        print("please provide valid source file")
        exit()
    
    old_fobj = open(file_name,"r")

    name, ext = os.path.splitext(file_name)

    new_file_name = "%s cleaned%s" %(name,ext)
    new_fobj = open(new_file_name,"w")

    for line in old_fobj:
        if line == "\n":
            continue
        else:
            new_fobj.write(line)
    
def main():

    if(len(sys.argv) == 1):
        print("Use the given flags as : ")
        print("--h is used to display the help")
        print("--u is used to display the usage")

    elif (len(sys.argv) == 2):
        if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):
            print("This application is used to remove all blank lines from a file")
        elif(sys.argv[1] == '--u' or sys.argv[1] == '--U'):
            print("Use the given script as ")
            print("Scriptname.py old_filename new_filename")
        else:
            RemoveBlankLines(sys.argv[1])
    
    

if __name__ == "__main__":
    main()