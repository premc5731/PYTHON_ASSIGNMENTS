# 7. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

def main():
    print("Enter a number : ",end="")
    Value = int(input())
    for i in range(Value):
        for j in range(1,Value+1):
            print(j,"",end="")
        print("")

if __name__ == "__main__":
    main()