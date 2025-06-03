# 7. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

def main():
    print("Enter a number : ",end="")
    value = int(input())
    for i in range(value):
        for j in range(1,value+1):
            print(j,"",end="")
        print("")

if __name__ == "__main__":
    main()