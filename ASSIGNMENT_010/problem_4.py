# 4.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce

Even = lambda x : (x % 2 == 0)

Square = lambda x : x**2

Summation = lambda x , y : x+y

def main():
    print("Enter size : ",end = "")
    size = int(input())

    Data = []

    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(Even,Data))
    print("Filtered Data : ",FData)
    
    MData = list(map(Square,FData))
    print("Mapped Data : ",MData)

    result = reduce(Summation,MData)
    print("Reduced result : ",result)

if __name__ == "__main__":
    main()