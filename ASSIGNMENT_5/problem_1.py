def Sum(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def Difference(No1,No2):
    Ans = 0
    Ans = No1 - No2
    return Ans

def Product(No1,No2):
    Ans = 0
    Ans = No1 * No2
    return Ans

def Division(No1,No2):
    Ans = 0
    try:
        Ans = No1 / No2
        return Ans
    except ArithmeticError:
        print("Invalid denominator")
    

def main():
    print("Enter first number : ",end="")
    Value1 = int(input())

    print("Enter second number : ",end="")
    Value2 = int(input())

    Result = 0

    Result = Sum(Value1,Value2)
    print("The Sum is : ",Result)

    Result = Difference(Value1,Value2)
    print("The Difference is : ",Result)

    Result = Product(Value1,Value2)
    print("The Product is : ",Result)

    Result = Division(Value1,Value2)
    print("The Division is : ",Result)

if __name__ == "__main__":
    main()
