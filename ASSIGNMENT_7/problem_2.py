# Q2. Accept a list of integers from the user and use the map() function to double each
# value.
# Expected Input:
# Enter list: 1 2 3 4 5
# Expected Output:
# Doubled list: [2, 4, 6, 8, 10]

double = lambda x: x*2

def main():
    Data = []
    print("Enter a number : ",end="")
    value = int(input())

    for i in range(value):
        Data.append(int(input()))

    MData = list(map(double,Data))

    print("Doubled list")
    print(MData)

if __name__ == "__main__":
    main()