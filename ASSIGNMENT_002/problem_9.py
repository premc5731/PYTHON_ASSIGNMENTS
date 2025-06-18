# 9. Write a program which accept number from user and return number of digits in that number.
# Input : 5187934 Output : 7
def Digits(no):
    no_digit = 0
    while(no != 0):
        no_digit +=1
        no = no // 10
    return no_digit

def main():
    print("Enter a number : ",end="")
    value = int(input())
    result = Digits(value)
    print("The number of digits : ",result)

if __name__ == "__main__":
    main()