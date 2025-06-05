def Sum(no1,no2):
    ans = 0
    ans = no1 + no2
    return ans

def Difference(no1,no2):
    ans = 0
    ans = no1 - no2
    return ans

def Product(no1,no2):
    ans = 0
    ans = no1 * no2
    return ans

def Division(no1,no2):
    ans = 0
    try:
        ans = no1 / no2
        return ans
    except ArithmeticError:
        print("Invalid denominator")
    

def main():
    print("Enter first number : ",end="")
    value1 = int(input())

    print("Enter second number : ",end="")
    value2 = int(input())

    result = 0

    result = Sum(value1,value2)
    print("The Sum is : ",result)

    result = Difference(value1,value2)
    print("The Difference is : ",result)

    result = Product(value1,value2)
    print("The Product is : ",result)

    result = Division(value1,value2)
    print("The Division is : ",result)

if __name__ == "__main__":
    main()
