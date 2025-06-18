# 5.Write a program which accept one number for user and check whether number is prime or not.
# Input : 5 Output : It is Prime Number

def CheckPrime(no):
    if no < 0:
        no = -no
        
    flag = True
    for i in range(2,no):
        if no % i == 0:
            flag = False
            break
    
    return flag


def main():
    print("Enter a number : ",end="")
    value = int(input())
    result = CheckPrime(value)
    if result == True:
        print("It is prime number")
    else:
        print("It is not prime number")

if __name__ == "__main__":
    main()