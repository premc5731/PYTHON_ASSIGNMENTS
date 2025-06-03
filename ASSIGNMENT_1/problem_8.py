# 8. Write a program which accept number from user and print that number of “*” on screen.
# Input : 5 Output : * * * * *

def StartPrint(no1):
    for i in range(0,no1):
        print("*",end="")

def main():
    print("Enter a number : ",end="")
    value1 = int(input())
    StartPrint(value1)

if __name__ == "__main__":
    main()