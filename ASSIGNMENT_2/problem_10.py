# 10. Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934 Output : 37

def Digits(No):
    DigitSum = 0
    Digit = 0
    while(No != 0):
        Digit = No % 10
        DigitSum = DigitSum + Digit
        No = No // 10
    return DigitSum

def main():
    print("Enter a number : ",end="")
    Value = int(input())
    Result = Digits(Value)
    print("The sum of digits is : ",Result)

if __name__ == "__main__":
    main()