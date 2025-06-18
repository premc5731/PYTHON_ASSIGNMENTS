# 7. Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 otherwise return false.
# Input : 8 Output : False
# Input : 25 Output : True

def DivisibleFive(no1):
    if (no1 % 5 == 0):
        return True
    else:
        return False
    
def main():
    print("Enter a number : ",end="")
    value = int(input())
    ret = DivisibleFive(value)
    print(ret)

if __name__ == "__main__":
    main()