# 3.Write a program which accept N numbers from user and store it into List. Return minimum
# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5

def main():
    print("Enter a number : ",end="")
    size = int(input())
    data = []
    min = float('inf')
    for i in range(size):
        data.append(int(input()))
    
    for i in range(size):
        if data[i] < min:
            min = data[i]

    print("minimum element is : ",min)

if __name__ == "__main__":
    main()