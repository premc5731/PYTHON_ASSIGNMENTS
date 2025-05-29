# Q2. Vowel or Consonant Check
# Accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not,
# print it's a consonant.
# Expected Input:
# Enter a character: e
# Expected Output:
# 'e' is a vowel.

def ChkVowel(c):
    Flag = False
    Vowel = "aeiouAEIOU"

    for v in Vowel:
        if v == c:
            Flag = True

    return Flag

def main():
    Ret = False
    print("Enter a character : ",end="")
    Value = input()
    Ret = ChkVowel(Value)

    if(Ret == True):
        print(f"{Value} is vowel")
    else:
        print(f"{Value} is consonant")


if __name__ == "__main__":
    main()