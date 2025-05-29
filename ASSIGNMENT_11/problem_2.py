# 2. Factorial Using Recursion
# Write a recursive function to calculate factorial of a number.
# factorial(5) → 120

Fact = 1
iCnt = 1

def Factorial(No):
    global Fact
    global iCnt

    # while(iCnt <= No):
    #     Fact = Fact * iCnt
    #     iCnt = iCnt + 1

    if(iCnt <= No):
        Fact = Fact * iCnt
        iCnt = iCnt + 1
        Factorial(No)

    return Fact

def main():
    Result = Factorial(5)
    print("Result : ",Result)

if __name__ == "__main__":
    main()
