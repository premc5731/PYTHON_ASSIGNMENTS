
# 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.

import calculator_module as calc

def main():
    print("Enter first number : ",end="")
    value1 = int(input())
    print("Enter second number : ",end="")
    value2 = int(input())

    result = calc.Add(value1,value2)
    print("Addition is : ",result)

    result = calc.Sub(value1,value2)
    print("Subraction is : ",result)

    result = calc.Mult(value1,value2)
    print("Multiplication is : ",result)

    result = calc.Div(value1,value2)
    print("Division is : ",result)

if __name__ == "__main__":
    main()
