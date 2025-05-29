# Q5. Write a function that accepts a string and checks whether it is a palindrome.
# Expected Input:
# Enter a string: radar
# Expected Output:
# radar is a palindrome.

def PalindromeCheck(Str):
    Flag = True
    start = 0
    end = len(Str)-1

    while(start < end):
        if Str[start] != Str[end]:
            Flag = False
            break
        start +=1
        end -=1

    return Flag

def main():
    print("Enter a string :",end="")
    iStr = input()

    Ret = PalindromeCheck(iStr)

    if Ret == True:
        print("It is palindrome")

    else:
        print("It is not palindrome")

if __name__ == "__main__":
    main()