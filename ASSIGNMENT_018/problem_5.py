# 5. Accept file name and one string from user and return the frequency of that string from file.
# Input : Demo.txt Marvellous
# Search “Marvellous” in Demo.txt


import sys
import os
        
def Frequency(file_name, str):
    freq = 0

    flag = os.path.exists(file_name)

    if(flag == False):
        print("Invalid file name")
        exit()
    fobj = open(file_name,"r")
    Buffer = fobj.read()

    Buffer  = Buffer.split()

    for word in Buffer:
        if word == str:
            freq += 1

    return freq

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
        ret = Frequency(sys.argv[1],sys.argv[2])

        print("the frequency of %s is %d"%(sys.argv[2],ret))

if __name__ == "__main__":
    main()