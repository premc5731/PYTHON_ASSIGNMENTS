# 5. Count Zeros in a Number (Recursively)
# Write a recursive function to count how many zeros are in the given number.
# count_zeros(1020300) → 4

icount = 0

def Count(no):
    global icount
    # while(no !=0):
    #     digit = no % 10
    #     if(digit == 0):
    #         Count +=1
    #     no = no // 10

    if(no !=0):
        digit = no % 10
        if(digit == 0):
            icount +=1
        no = no // 10
        Count(no)
        
    return icount

def main():
    result = Count(1020300)
    print("no of zeros are : ",result)

if __name__ == "__main__":
    main()