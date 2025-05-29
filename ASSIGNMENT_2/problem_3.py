# 3. Write a program which accept one number from user and return its factorial.
# Input : 5 Output : 120

def Factorial(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    print("Enter a number : ",end="")
    Value = int(input())
    Result = Factorial(Value)
    print(f"The factorial of {Value} is : ",Result)

if __name__ == "__main__":
    main()