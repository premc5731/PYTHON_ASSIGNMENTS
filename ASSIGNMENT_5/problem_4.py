# Q4. Find Largest Among Three Numbers
# Accept three numbers from the user and print the largest using nested if-else statements.
# Expected Input:
# Enter three numbers: 5 9 3
# Expected Output:
# Largest number is 9.

def Largest(No1, No2, No3):
    LValue = 0
    if No1 > No2:
        if No1 > No3:
            LValue = No1
    elif No2 > No3:
        LValue = No2
    else:
        LValue = No3

    return LValue


def main():
    Value1 = 0
    Value2 = 0
    Value3 = 0
    Ret = 0

    print("Enter first number : ",end="")
    Value1 = int(input())

    print("Enter second number : ",end="")
    Value2 = int(input())

    print("Enter third number : ",end="")
    Value3 = int(input())

    Ret = Largest(Value1,Value2,Value3)

    print("Largest number is : ",Ret)

if __name__ == "__main__":
    main()