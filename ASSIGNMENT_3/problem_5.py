# 5.Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 32 (13 + 5 + 7 +2 + 5)
import MARVELLOUSNUM 

def ListPrime(data):
    sum = 0
    for i in range(len(data)):
        if MARVELLOUSNUM.ChkPrime(data[i]):
            sum = sum + data[i]

    return sum

def main():
    data = []
    print("Enter a number : ",end="")
    size = int(input())

    for i in range(size):
        data.append(int(input()))

    result = ListPrime(data)
    print("The summation of prime numbers is : ",result)


if __name__ == "__main__":
    main()