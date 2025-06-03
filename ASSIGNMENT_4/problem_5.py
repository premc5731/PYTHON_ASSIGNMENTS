# 5.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce


def CheckPrime(No):
    flag = True
    for i in range(2,(No//2)+1):
        if(No % i == 0):
            flag = False
            break
    
    return flag

def Mult(No):
    return (No * 2)

def Max(no1,no2):
    if(no1 > no2):
        return no1
    else:
        return no2
    

def main():
    Data = []
    print("Enter size : ",end="")
    size = int(input())

    print("Enter numbers : ")
    for i in range(size):
        element = int(input())
        Data.append(element)

    FData = list(filter(CheckPrime,Data))
    print("Filtered Data : ",FData)

    MData = list(map(Mult,FData))
    print("Mapped Data : ",MData)

    RData = reduce(Max,MData)
    print("The Result is : ",RData)

    
if __name__ == "__main__":
    main()