# 4.Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def main():
    Data = []
    Max = -float('inf')
    freq = 0

    print("Enter a number : ",end="")
    Size = int(input())
    
    for i in range(Size):
        Data.append(int(input()))

    print("Element to search : ",end="")
    search = int(input())

    for i in Data:
        if Data[i] == search:
            freq += 1
            
    print("Frequency is : ",freq)


if __name__ == "__main__":
    main()