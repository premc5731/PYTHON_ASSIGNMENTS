# 2.Write a program which accept N numbers from user and store it into List. Return maximum
# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

def main():
    print("Enter a number : ",end="")
    size = int(input())
    data = []
    max = -float('inf')
    for i in range(size):
        data.append(int(input()))
    
    for i in range(size):
        if data[i] > max:
            max = data[i]

    print("maximum element is : ",max)

if __name__ == "__main__":
    main()