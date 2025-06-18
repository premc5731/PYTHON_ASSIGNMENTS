# 4.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce


CheckEven = lambda no: no % 2 == 0
Square = lambda no: no**2
Sum = lambda no1,no2: no1 + no2

def main():
    data = []
    print("Enter size : ",end="")
    size = int(input())

    print("Enter numbers : ")
    for i in range(size):
        element = int(input())
        data.append(element)

    Fdata = list(filter(CheckEven,data))
    print("Filtered data : ",Fdata)

    Mdata = list(map(Square,Fdata))
    print("Mapped data : ",Mdata)

    Rdata = reduce(Sum,Mdata)
    print("The Result is : ",Rdata)

    
if __name__ == "__main__":
    main()