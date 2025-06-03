# 4.Write a program which accept one number form user and return addition of its factors.
# Input : 12 Output : 16 (1+2+3+4+6)
def Factorssum(no):
    sum = 0
    if no < 0:
        no = -no
    for i in range(1,(int((no/2))+1)):
        print("i",i)
        if no % i == 0:
            sum = sum + i

    return sum

def main():
    print("Enter a number : ",end="")
    value = int(input())
    result = Factorssum(value)
    print("summation of factors is : ",result)

if __name__ == "__main__":
    main()