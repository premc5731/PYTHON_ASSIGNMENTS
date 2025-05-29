# Q5. Even or Odd Number Check
# Write a program to check whether the entered number is even or odd.
# Expected Input:
# Enter a number: 17
# Expected Output:
# 17 is an odd number.

def CheckEven(No):
    Result = False

    if No % 2 == 0:
        Result = True
    
    return Result

def main():
    Ret = False
    print("Enter a number : ",end="")
    Value = int(input())

    Ret = CheckEven(Value)

    if Ret == True:
        print(f"{Value} is Even")

    else:
        print(f"{Value} is Odd")

if __name__ == "__main__":
    main()