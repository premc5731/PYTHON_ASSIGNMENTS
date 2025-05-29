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
    Value = int(input())

    SRet = square(Value)
    CRet = cube(Value)

    print("Square of {} is {}".format(Value,SRet))
    print("Cube of {} is {}".format(Value,CRet))    

if __name__ == "__main__":
    main()