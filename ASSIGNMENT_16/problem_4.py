# 4. Accept 10 numbers from the user and write them into a file named numbers.txt,
# each on a new line.

import os

def Number(file_name):
    flag = os.path.exists(file_name)

    if(flag == True):
        print("Filename must me unique ")
        exit()
    fobj = open(file_name,"w")

    print("Enter numbers : ")
    for i in range(0,10):
        print("Number ",i+1," : ",end="")
        no = input()
        no = no + "\n"
        fobj.write(no)
    

    print("Records sucessfully saved")

def main():
    print("Enter the new file name : ",end = "")
    fname = input()

    Number(fname)

if __name__ == "__main__":
    main()