# Q2. vowel or Consonant Check
# Accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not,
# print it's a consonant.
# Expected Input:
# Enter a character: e
# Expected Output:
# 'e' is a vowel.

def Chkvowel(c):
    flag = False
    vowel = "aeiouAEIOU"

    for v in vowel:
        if v == c:
            flag = True

    return flag

def main():
    ret = False
    print("Enter a character : ",end="")
    value = input()
    ret = Chkvowel(value)

    if(ret == True):
        print(f"{value} is vowel")
    else:
        print(f"{value} is consonant")


if __name__ == "__main__":
    main()