# 3. Write a program which contains one function named as Add() which accepts two numbers
# from user and return addition of that two numbers.
# Input : 11 5 Output : 16



def Add(No1,No2):
    result = 0.0
    result = No1 + No2
    return result

def main():
    print("Enter the first number : ", end="")
    Value1 = int(float(input()))
    print("Enter the second number : ", end="")
    Value2 = int(float(input()))
    result = 0
    result = Add(Value1, Value2)
    print("The result is :",result)


if __name__ == "__main__":
    main()    