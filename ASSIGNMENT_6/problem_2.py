# Q2. Print Sum of Even Numbers Between 1 and 100. Use a loop to find and print the sum
# of all even numbers from 1 to 100.
# Expected Output:
# Sum of even numbers between 1 to 100 is: 2550

def SumEven():
    Sum = 0
    for i in range(1,101):
        if i % 2 == 0:
            Sum = Sum + i

    return Sum

def main():
    Ret = SumEven()
    print("Sum of even numbers between 1 and 100 is :",Ret)

if __name__ == "__main__":
    main()