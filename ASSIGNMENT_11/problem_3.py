# 3. Sum of Digits
# Write a recursive function to calculate the sum of digits of a number.
# sum_of_digits(1234) → 10

Sum = 0
def SumDigits(No):
    global Sum

    # while(No != 0):
    #     Digit = No % 10
    #     Sum = Sum + Digit
    #     No = No // 10

    if(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10
        SumDigits(No)

    return Sum

def main():
    Result = SumDigits(1234)
    print("Result : ",Result)

if __name__ == "__main__":
    main()