# Q3. Voting Eligibility Checker
# Accept age from the user and check whether the person is eligible to vote. (Age should be
# 18 or above.)
# Expected Input:
# Enter age: 19
# Expected Output:
# Eligible to vote.

def VotAgeCheck(no):
    result = True
    if no < 18:
        result = False

    return result
def main():
    ret = 0
    print("Enter your age : ",end = "")
    age = int(input())

    ret = VotAgeCheck(age)

    if(ret == True):
        print("Eligible to vote")
    else:
        print("not Eligible to vote")
       
if __name__ == "__main__":
    main()