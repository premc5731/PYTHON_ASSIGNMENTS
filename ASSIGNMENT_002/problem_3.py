# 3. Write a program which accept one number from user and return its factorial.
# Input : 5 Output : 120

def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i

    return fact

def main():
    print("Enter a number : ",end="")
    value = int(input())
    result = factorial(value)
    print(f"The factorial of {value} is : ",result)

if __name__ == "__main__":
    main()