# Q4. Accept a number and print its factorial using a for loop.
# Expected Input:
# Enter a number: 5
# Expected Output:
# factorial of 5 is: 120

def factorial(no):

    if( no < 0):
        print("Invalid input")
        return
    
    fact = 1

    for i in range(1,no+1):
        fact = fact * i

    return fact

def main():
    print("Enter a number : ",end="")
    value = int(input())
    ret = factorial(value)

    print("factorial of {} is {}".format(value,ret))
    

if __name__ == "__main__":
    main()