# Q6. Write a function that accepts a list of integers and returns a list of prime numbers
# using filter().
# Expected Input:
# Enter list: 10 11 12 13 14 15 16 17
# Expected Output:
# Prime numbers: [11, 13, 17]

def ChkPrime(no):
    flag = True
    for i in range(2,(no//2)+1):
        if no % i == 0:
            flag = False
            break

    return flag

def main():
    Data = []
    print("Enter a number : ",end="")
    value = int(input())

    for i in range(value):
        Data.append(int(input()))

    FData = list(filter(ChkPrime,Data))

    print("Prime number list is")
    print(FData)
    

if __name__ == "__main__":
    main()