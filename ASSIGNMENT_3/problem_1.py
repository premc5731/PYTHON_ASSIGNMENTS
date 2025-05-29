# 1.Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130
def main():
    print("Enter a number : ",end="")
    Size = int(input())
    Data = []
    Sum = 0
    for i in range(Size):
        Data.append(int(input()))
    for i in Data:
        Sum = Sum + i
    print("Summation is : ",Sum)


if __name__ == "__main__":
    main()