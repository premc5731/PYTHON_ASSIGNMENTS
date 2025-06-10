# 7. Create a file marks.txt with student name and marks. Then read the file and
# display students who scored more than 75 marks.

import os

def Display(file_name):
    fobj = open(file_name,"r")
    Buffer = fobj.read()
    Buffer = Buffer.split("\n")
    for i in range(len(Buffer) - 1):
        record = Buffer[i].split(": ")
        marks = int(record[1])

        if(marks > 75):
            print(Buffer[i])


def CreateFile(file_name):
    flag = os.path.exists(file_name)

    if flag == True:
        print("filename already exists")
        print("filename must be unique")
        exit()
    fobj = open(file_name,"x")

    print("Enter the number of students : ",end ="")
    size = int(input())

    print("Enter student record format must be ")
    print("student_name : student_marks")

    for i in range(size):
        print("student ",i+1," : ",end ="")
        record = input()
        record = record + "\n"
        fobj.write(record)
    print("Student record saved sucessfully")


def main():
    print("Enter the new file name that you want to create ", end ="")
    fname = input()
    CreateFile(fname)
    print("students who scored more than 75 ")
    Display(fname)

if __name__ == "__main__":
    main()
