# 5.Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 32 (13 + 5 + 7 +2 + 5)
import MARVELLOUSNUM 

def ListPrime(Data):
    Sum = 0
    for i in range(len(Data)):
        if MARVELLOUSNUM.ChkPrime(Data[i]):
            Sum = Sum + Data[i]

    return Sum

def main():
    Data = []
    print("Enter a number : ",end="")
    Size = int(input())

    for i in range(Size):
        Data.append(int(input()))

    Result = ListPrime(Data)
    print("The summation of prime numbers is : ",Result)


if __name__ == "__main__":
    main()