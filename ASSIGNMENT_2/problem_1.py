
# 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.

import calculator_module as calc

def main():
    print("Enter first number : ",end="")
    Value1 = int(input())
    print("Enter second number : ",end="")
    Value2 = int(input())

    Result = calc.Add(Value1,Value2)
    print("Addition is : ",Result)

    Result = calc.Sub(Value1,Value2)
    print("Subraction is : ",Result)

    Result = calc.Mult(Value1,Value2)
    print("Multiplication is : ",Result)

    Result = calc.Div(Value1,Value2)
    print("Division is : ",Result)

if __name__ == "__main__":
    main()
