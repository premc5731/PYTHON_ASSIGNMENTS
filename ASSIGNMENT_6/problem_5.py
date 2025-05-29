# Q5. Accept a number from the user and check whether it is prime or not.
# Expected Input:
# Enter a number: 11
# Expected Output:
# 11 is a prime number.

def ChkPrime(No):
    if No < 0:
        No = -No
        
    Flag = True

    for i in range(2, (No//2)+1):
        if No % i == 0:
            Flag = False
            break

    return Flag

def main():
    print("Enter a number : ",end="")
    Value = int(input())

    Ret = ChkPrime(Value)

    if Ret == True:
        print("It is prime number")
    else:
        print("It is Not a prime number")
    

if __name__ == "__main__":
    main()