# Q3. Accept a number from the user and print its multiplication table up to 10.
# Expected Input:
# Enter a number: 7
# Expected Output
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

def Multiplication(no):

    for i in range(1,11):
        print(no," x ",i," = ",(no*i))
    

def main():
    print("Enter a number : ",end="")
    value = int(input())
    Multiplication(value)

if __name__ == "__main__":
    main()