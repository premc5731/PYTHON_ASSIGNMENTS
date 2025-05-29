# 6. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 
# * * * * *
# * * * *
# * * *
# * *
# *

def main():
    print("Enter a number : ",end="")
    Value = int(input())

    for i in range(Value):
        for j in range(i,Value):
            print("*",end="")
        print("")

if __name__ == "__main__":
    main()