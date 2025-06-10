# 2. Write a program which accept file name from user and open that file and display the contents
# of that file on screen.
# Input : Demo.txt
# Display contents of Demo.txt on console.

import os

def Display(file_name):

    flag = os.path.exists(file_name)

    if flag == False:
        print("file is not present in current directory")
        exit()
    elif flag == True:
        fobj = open(file_name,"r")
        Buffer = fobj.read()
        print(Buffer)

def main():
    print("Enter the file name to display : ",end = "")
    fname = input()

    Display(fname)

if __name__ == "__main__":
    main()