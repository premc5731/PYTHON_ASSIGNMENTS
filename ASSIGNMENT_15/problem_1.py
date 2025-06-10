# 1.Write a program which accepts file name from user and check whether that file exists in
# current directory or not.
# Input : Demo.txt
# Check whether Demo.txt exists or not.


import os

def is_exists(file_name):
    flag = False

    flag = os.path.exists(file_name)
    
    return flag

def main():
    print("Enter the file name : ",end = "")
    fname = input()

    ret = is_exists(fname)

    if ret == True:
        print(fname," file present in current directory")
    else:
        print(fname," file is not present in current directory")
    

if __name__ == "__main__":
    main()