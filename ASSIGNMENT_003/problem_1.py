# 1.Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130
def main():
    print("Enter a number : ",end="")
    size = int(input())
    data = []
    sum = 0
    for i in range(size):
        data.append(int(input()))
    for i in data:
        sum = sum + i
    print("summation is : ",sum)


if __name__ == "__main__":
    main()