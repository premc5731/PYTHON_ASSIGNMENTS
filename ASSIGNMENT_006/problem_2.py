# Q2. Print sum of Even Numbers Between 1 and 100. Use a loop to find and print the sum
# of all even numbers from 1 to 100.
# Expected Output:
# sum of even numbers between 1 to 100 is: 2550

def sumEven():
    sum = 0
    for i in range(1,101):
        if i % 2 == 0:
            sum = sum + i

    return sum

def main():
    ret = sumEven()
    print("sum of even numbers between 1 and 100 is :",ret)

if __name__ == "__main__":
    main()