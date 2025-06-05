# Q5. Even or Odd Number Check
# Write a program to check whether the entered number is even or odd.
# Expected Input:
# Enter a number: 17
# Expected Output:
# 17 is an odd number.

def CheckEven(no):
    result = False

    if no % 2 == 0:
        result = True
    
    return result

def main():
    ret = False
    print("Enter a number : ",end="")
    value = int(input())

    ret = CheckEven(value)

    if ret == True:
        print(f"{value} is Even")

    else:
        print(f"{value} is Odd")

if __name__ == "__main__":
    main()