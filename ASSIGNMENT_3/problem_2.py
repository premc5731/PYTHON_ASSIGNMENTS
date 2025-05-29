# 2.Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

def main():
    print("Enter a number : ",end="")
    Size = int(input())
    Data = []
    Max = -float('inf')
    for i in range(Size):
        Data.append(int(input()))
    
    for i in range(Size):
        if Data[i] > Max:
            Max = Data[i]

    print("Maximum element is : ",Max)

if __name__ == "__main__":
    main()