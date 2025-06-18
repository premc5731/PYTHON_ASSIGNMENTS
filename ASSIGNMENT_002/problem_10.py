# 10. Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934 Output : 37

def digits(no):
    digit_sum = 0
    digit = 0
    while(no != 0):
        digit = no % 10
        digit_sum = digit_sum + digit
        no = no // 10
    return digit_sum

def main():
    print("Enter a number : ",end="")
    value = int(input())
    result = digits(value)
    print("The sum of digits is : ",result)

if __name__ == "__main__":
    main()