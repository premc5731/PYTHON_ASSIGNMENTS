# 4.Write a program which accept one number form user and return addition of its factors.
# Input : 12 Output : 16 (1+2+3+4+6)
def FactorsSum(No):
    Sum = 0
    if No < 0:
        No = -No
    for i in range(1,(int((No/2))+1)):
        print("i",i)
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
    print("Enter a number : ",end="")
    value = int(input())
    Result = FactorsSum(value)
    print("Summation of factors is : ",Result)

if __name__ == "__main__":
    main()