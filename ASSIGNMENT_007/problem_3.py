# Q3. Accept a list of numbers and use filter() to keep only even numbers.
# Expected Input:
# Enter list: 1 2 3 4 5 6
# Expected Output:
# Even numbers: [2, 4, 6]

Even = lambda x: x % 2 == 0

def main():
    Data = []
    print("Enter a number : ",end="")
    value = int(input())

    for i in range(value):
        Data.append(int(input()))

    FData = list(filter(Even,Data))

    print("Eveen numbers list is")
    print(FData)
    

if __name__ == "__main__":
    main()