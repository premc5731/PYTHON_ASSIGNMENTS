# 2.Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.
# Input : 4 3 Output : 12
# Input : 6 3 Output : 18

Mult = lambda x , y: x*y

def main():
    print("Enter first number : ",end="")
    Value1 = int(input())

    print("Enter second number : ",end="")
    Value2 = int(input())

    Ret = Mult(Value1,Value2)
    print("Multiplication is ",Ret)

if __name__ == "__main__":
    main()