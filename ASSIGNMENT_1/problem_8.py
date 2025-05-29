# 8. Write a program which accept number from user and print that number of “*” on screen.
# Input : 5 Output : * * * * *

def StartPrint(No1):
    for i in range(0,No1):
        print("*",end="")

def main():
    print("Enter a number : ",end="")
    Value1 = int(input())
    StartPrint(Value1)

if __name__ == "__main__":
    main()