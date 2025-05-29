# Q3. Voting Eligibility Checker
# Accept age from the user and check whether the person is eligible to vote. (Age should be
# 18 or above.)
# Expected Input:
# Enter age: 19
# Expected Output:
# Eligible to vote.

def VotAgeCheck(No):
    Result = True
    if No < 18:
        Result = False

    return Result
def main():
    Ret = 0
    print("Enter your age : ",end = "")
    age = int(input())

    Ret = VotAgeCheck(age)

    if(Ret == True):
        print("Eligible to vote")
    else:
        print("Not Eligible to vote")
       
if __name__ == "__main__":
    main()