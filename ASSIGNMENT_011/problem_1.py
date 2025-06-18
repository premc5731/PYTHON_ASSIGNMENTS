# 1. Print Numbers Using Recursion
# Write a recursive function to print numbers from 1 to N.
# Expected Output (for n=5):
# 1 2 3 4 5

icnt = 1
def Display(no):
    # icnt = 1
    # while(icnt <= no):
    #     print(icnt)
    #     icnt += 1
    global icnt
    if(icnt <= no):
        print(icnt)
        icnt += 1
        Display(no)

def main():
    Display(5)

if __name__ == "__main__":
    main()