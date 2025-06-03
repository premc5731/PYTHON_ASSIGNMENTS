# 6.Write a program which accept number from user and check whether that number is positive or
# negative or zero.
# Input : 11 Output : Positive Number
# Input : -8 Output : Negative Number
# Input : 0 Output : Zero

def CheckNumber(no1):
    if no1 == 0:
        print("Zero")
    elif no1 < 0:
        print("Negative")
    else:
        print("Positive")

def main():
    print("Enter a number : ",end="")
    value1 = int(input())
    CheckNumber(value1)

if __name__ == "__main__":
    main()    