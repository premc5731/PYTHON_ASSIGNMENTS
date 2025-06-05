# Q5. Write a function that accepts a string and checks whether it is a palindrome.
# Expected Input:
# Enter a string: radar
# Expected Output:
# radar is a palindrome.

def PalindromeCheck(str):
    flag = True
    start = 0
    end = len(str)-1

    while(start < end):
        if str[start] != str[end]:
            flag = False
            break
        start +=1
        end -=1

    return flag

def main():
    print("Enter a string :",end="")
    istr = input()

    ret = PalindromeCheck(istr)

    if ret == True:
        print("It is palindrome")

    else:
        print("It is not palindrome")

if __name__ == "__main__":
    main()