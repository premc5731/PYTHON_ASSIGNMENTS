# Q4. Accept a number and print its factorial using a for loop.
# Expected Input:
# Enter a number: 5
# Expected Output:
# Factorial of 5 is: 120

def Factorial(No):

    if( No < 0):
        print("Invalid input")
        return
    
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    print("Enter a number : ",end="")
    Value = int(input())
    Ret = Factorial(Value)

    print("Factorial of {} is {}".format(Value,Ret))
    

if __name__ == "__main__":
    main()