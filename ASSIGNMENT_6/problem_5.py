# Q5. Accept a number from the user and check whether it is prime or not.
# Expected Input:
# Enter a number: 11
# Expected Output:
# 11 is a prime number.

def ChkPrime(no):
    if no < 0:
        no = -no
        
    flag = True

    for i in range(2, (no//2)+1):
        if no % i == 0:
            flag = False
            break

    return flag

def main():
    print("Enter a number : ",end="")
    value = int(input())

    ret = ChkPrime(value)

    if ret == True:
        print("It is prime number")
    else:
        print("It is not a prime number")
    

if __name__ == "__main__":
    main()