# 1.Write a program which contains one lambda function which accepts one parameter and return
# power of two.
# Input : 4 Output : 16
# Input : 6 Output : 64

Power = lambda x : x**2

def main():
    print("Enter a number : ",end="")
    value = int(input())

    ret = Power(value)
    print("Power of {} is {}".format(value,ret))

if __name__ == "__main__":
    main()