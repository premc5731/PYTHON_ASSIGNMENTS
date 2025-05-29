# Q6. Write a function that accepts a list of integers and returns a list of prime numbers
# using filter().
# Expected Input:
# Enter list: 10 11 12 13 14 15 16 17
# Expected Output:
# Prime numbers: [11, 13, 17]

def ChkPrime(No):
    Flag = True
    for i in range(2,(No//2)+1):
        if No % i == 0:
            Flag = False
            break

    return Flag

def main():
    Data = []
    print("Enter a number : ",end="")
    Value = int(input())

    for i in range(Value):
        Data.append(int(input()))

    FData = list(filter(ChkPrime,Data))

    print("Prime number list is")
    print(FData)
    

if __name__ == "__main__":
    main()