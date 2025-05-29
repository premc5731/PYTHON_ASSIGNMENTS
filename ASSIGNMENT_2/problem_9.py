# 9. Write a program which accept number from user and return number of digits in that number.
# Input : 5187934 Output : 7
def Digits(No):
    NoDigit = 0
    while(No != 0):
        NoDigit +=1
        No = No // 10
    return NoDigit

def main():
    print("Enter a number : ",end="")
    Value = int(input())
    Result = Digits(Value)
    print("The number of digits : ",Result)

if __name__ == "__main__":
    main()