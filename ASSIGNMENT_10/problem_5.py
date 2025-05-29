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

def Prime(No):
    Flag = True

    for i in range(2,(No // 2)+1):
        if(No % i == 0):
            Flag = False
            break

    return Flag

Mult = lambda x : x*2

def Maximum(No1,No2):
    if(No1 > No2):
        return No1
    else:
        return No2

def main():
    print("Enter size : ",end = "")
    size = int(input())

    Data = []

    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(Prime,Data))
    print("Filtered Data : ",FData)
    
    MData = list(map(Mult,FData))
    print("Mapped Data : ",MData)

    Result = reduce(Maximum,MData)
    print("Reduced result : ",Result)

if __name__ == "__main__":
    main()