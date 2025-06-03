# 4.Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def main():
    data = []
    max = -float('inf')
    freq = 0

    print("Enter a number : ",end="")
    size = int(input())
    
    for i in range(size):
        data.append(int(input()))

    print("Element to search : ",end="")
    search = int(input())

    for i in data:
        if data[i] == search:
            freq += 1
            
    print("Frequency is : ",freq)


if __name__ == "__main__":
    main()