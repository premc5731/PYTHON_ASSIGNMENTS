# Q4. Find Largest Among Three Numbers
# Accept three numbers from the user and print the largest using nested if-else statements.
# Expected Input:
# Enter three numbers: 5 9 3
# Expected Output:
# Largest number is 9.

def Largest(no1, no2, no3):
    lvalue = 0
    if no1 > no2:
        if no1 > no3:
            lvalue = no1
    elif no2 > no3:
        lvalue = no2
    else:
        lvalue = no3

    return lvalue


def main():
    value1 = 0
    value2 = 0
    value3 = 0
    ret = 0

    print("Enter first number : ",end="")
    value1 = int(input())

    print("Enter second number : ",end="")
    value2 = int(input())

    print("Enter third number : ",end="")
    value3 = int(input())

    ret = Largest(value1,value2,value3)

    print("Largest number is : ",ret)

if __name__ == "__main__":
    main()