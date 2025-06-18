# 3.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

RangeChk = lambda x : ((x >= 70) and (x <= 90))

Sum = lambda x : x+10

Product = lambda x , y : x*y

def main():
    print("Enter size : ",end = "")
    size = int(input())

    Data = []

    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(RangeChk,Data))
    print("Filtered Data : ",FData)
    
    MData = list(map(Sum,FData))
    print("Mapped Data : ",MData)

    Result = reduce(Product,MData)
    print("Reduced result : ",Result)

if __name__ == "__main__":
    main()