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
    value = int(input())

    for i in range(value):
        for j in range(i,value):
            print("*",end="")
        print("")

if __name__ == "__main__":
    main()