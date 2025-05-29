# 3.Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5

def main():
    print("Enter a number : ",end="")
    Size = int(input())
    Data = []
    Min = float('inf')
    for i in range(Size):
        Data.append(int(input()))
    
    for i in range(Size):
        if Data[i] < Min:
            Min = Data[i]

    print("Minimum element is : ",Min)

if __name__ == "__main__":
    main()