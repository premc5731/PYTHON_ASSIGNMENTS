# 4. Power Function Using Recursion
# Write a recursive function to calculate x^n.
# power(2, 3) → 8


iCnt = 1
Result = 1

def Power(X,N):
    global iCnt,Result

    # while(iCnt <= N):
    #     Result= Result * X
    #     iCnt += 1

    if(iCnt <= N):
        Result= Result * X
        iCnt += 1
        Power(X,N)

    return Result
def main():
    Result = Power(2,3)
    print("Result : ",Result)

if __name__ == "__main__":
    main()