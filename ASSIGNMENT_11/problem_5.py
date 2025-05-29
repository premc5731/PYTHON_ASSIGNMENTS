# 5. Count Zeros in a Number (Recursively)
# Write a recursive function to count how many zeros are in the given number.
# count_zeros(1020300) → 4

iCount = 0

def Count(No):
    global iCount
    # while(No !=0):
    #     Digit = No % 10
    #     if(Digit == 0):
    #         Count +=1
    #     No = No // 10

    if(No !=0):
        Digit = No % 10
        if(Digit == 0):
            iCount +=1
        No = No // 10
        Count(No)
        
    return iCount

def main():
    Result = Count(1020300)
    print("no of zeros are : ",Result)

if __name__ == "__main__":
    main()