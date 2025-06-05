# 3. sum of digits
# Write a recursive function to calculate the sum of digits of a number.
# sum_of_digits(1234) → 10

sum = 0
def SumDigits(no):
    global sum

    # while(no != 0):
    #     digit = no % 10
    #     sum = sum + digit
    #     no = no // 10

    if(no != 0):
        digit = no % 10
        sum = sum + digit
        no = no // 10
        SumDigits(no)

    return sum

def main():
    result = SumDigits(1234)
    print("result : ",result)

if __name__ == "__main__":
    main()