# 1. Print Numbers Using Recursion
# Write a recursive function to print numbers from 1 to N.
# Expected Output (for n=5):
# 1 2 3 4 5

iCnt = 1
def Display(No):
    # iCnt = 1
    # while(iCnt <= No):
    #     print(iCnt)
    #     iCnt += 1
    global iCnt
    if(iCnt <= No):
        print(iCnt)
        iCnt += 1
        Display(No)

def main():
    Display(5)

if __name__ == "__main__":
    main()