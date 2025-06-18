# 1. Write a Python program to create a text file named student.txt and write the
# names of 5 students into it.

import os

def StudentRecord(file_name):
    flag = os.path.exists(file_name)

    if(flag == True):
        print("Filename must me unique ")
        exit()
    fobj = open(file_name,"w")

    print("Enter student names")
    for i in range(0,5):
        print("Student ",i+1," : ",end="")
        name = input()
        name = name + "\n"
        fobj.write(name)
    

    print("Records sucessfully saved")

def main():
    print("Enter the new file name : ",end = "")
    fname = input()

    StudentRecord(fname)

if __name__ == "__main__":
    main()