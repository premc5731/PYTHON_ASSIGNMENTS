# Q4. Accept a list of numbers and use reduce() (from functools) to find the product of
# all numbers.
# Expected Input:
# Enter list: 2 3 4
# Expected Output:
# Product: 24

from functools import reduce


product = lambda x,y: x*y

def main():
    Data = []
    print("Enter a number : ",end="")
    value = int(input())

    for i in range(value):
        Data.append(int(input()))

    result = reduce(product,Data)

    print("Product of numbers is : ",result)

if __name__ == "__main__":
    main()