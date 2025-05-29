# 1.Write a program which contains one lambda function which accepts one parameter and return
# power of two.
# Input : 4 Output : 16
# Input : 6 Output : 64

Power = lambda x : x**2

def main():
    print("Enter a number : ",end="")
    Value = int(input())

    Ret = Power(Value)
    print("Power of {} is {}".format(Value,Ret))

if __name__ == "__main__":
    main()