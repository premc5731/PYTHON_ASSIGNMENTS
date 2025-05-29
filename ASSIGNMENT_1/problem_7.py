# 7. Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 otherwise return false.
# Input : 8 Output : False
# Input : 25 Output : True

def DivisibleFive(No1):
    if (No1 % 5 == 0):
        return True
    else:
        return False
    
def main():
    print("Enter a number : ",end="")
    Value1 = int(input())
    Ret = DivisibleFive(Value1)
    print(Ret)

if __name__ == "__main__":
    main()