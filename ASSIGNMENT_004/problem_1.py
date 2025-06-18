# 1.Write a program which contains one lambda function which accepts one parameter and return
# power of two.
# Input : 4 Output : 16
# Input : 6 Output : 64

def main():
    print("Enter a number : ",end = "")
    value = int(input())
    square = lambda x: 2**x
    result = square(value)
    
    print(f"The result is : {result}")


if __name__ == "__main__":
    main()