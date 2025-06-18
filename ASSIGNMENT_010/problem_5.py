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

def Prime(no):
    flag = True

    for i in range(2,(no // 2)+1):
        if(no % i == 0):
            flag = False
            break

    return flag

Mult = lambda x : x*2

def Maximum(no1,no2):
    if(no1 > no2):
        return no1
    else:
        return no2

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

    result = reduce(Maximum,MData)
    print("Reduced result : ",result)

if __name__ == "__main__":
    main()