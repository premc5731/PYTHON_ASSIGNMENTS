# 2.Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.
# Input : 4 3 Output : 12
# Input : 6 3 Output : 18

def main():
    print("Enter first number : ",end = "")
    value1 = int(input())
    print("Enter second number : ",end = "")
    value2 = int(input())
    mult = lambda No1,No2: No1*No2
    result = mult(value1,value2)
    
    print(f"The multiplication is : {result}")


if __name__ == "__main__":
    main()