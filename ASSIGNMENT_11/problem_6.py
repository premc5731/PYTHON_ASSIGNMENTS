# 6. Sum of First N Natural Numbers
# Write a recursive function to calculate sum from 1 to n.
# sum_n(5) → 15

Sum = 0
iCnt = 1

def SumN(No):
    global Sum, iCnt

    if(iCnt <= No):
        Sum = Sum + iCnt
        iCnt += 1
        SumN(No)

    return Sum


def main():
    Result = SumN(5)
    print("Sum of natural numbers is : ",Result)

if __name__ == "__main__":
    main()