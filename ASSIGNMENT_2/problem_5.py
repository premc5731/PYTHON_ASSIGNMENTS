# 5.Write a program which accept one number for user and check whether number is prime or not.
# Input : 5 Output : It is Prime Number

def CheckPrime(No):
    if No < 0:
        No = -No
        
    Flag = True
    for i in range(2,No):
        if No % i == 0:
            Flag = False
            break
    
    return Flag


def main():
    print("Enter a number : ",end="")
    Value = int(input())
    Result = CheckPrime(Value)
    if Result == True:
        print("It is prime number")
    else:
        print("It is not prime number")

if __name__ == "__main__":
    main()