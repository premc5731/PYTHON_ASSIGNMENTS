# Q1. Write two lambda functions:
# • One to calculate square of a number
# • Another to calculate cube of a number
# Expected Input:
# Enter a number: 3
# Expected Output:
# Square: 9
# Cube: 27

square = lambda x: x**2

cube = lambda x: x**3

def main():
    print("Enter a number : ",end="")
    value = int(input())

    SRet = square(value)
    CRet = cube(value)

    print("Square of {} is {}".format(value,SRet))
    print("Cube of {} is {}".format(value,CRet))    

if __name__ == "__main__":
    main()