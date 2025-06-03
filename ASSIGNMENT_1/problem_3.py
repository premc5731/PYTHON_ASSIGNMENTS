# 3. Write a program which contains one function named as Add() which accepts two numbers
# from user and return addition of that two numbers.
# Input : 11 5 Output : 16



def Add(no1,no2):
    result = 0.0
    result = no1 + no2
    return result

def main():
    print("Enter the first number : ", end="")
    value1 = int(float(input()))
    print("Enter the second number : ", end="")
    value2 = int(float(input()))
    result = 0
    result = Add(value1, value2)
    print("The result is :",result)


if __name__ == "__main__":
    main()    