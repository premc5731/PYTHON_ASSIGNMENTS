# 2. factorial Using Recursion
# Write a recursive function to calculate factorial of a number.
# factorial(5) → 120

fact = 1
icnt = 1

def factorial(no):
    global fact
    global icnt

    # while(icnt <= no):
    #     fact = fact * icnt
    #     icnt = icnt + 1

    if(icnt <= no):
        fact = fact * icnt
        icnt = icnt + 1
        factorial(no)

    return fact

def main():
    result = factorial(5)
    print("result : ",result)

if __name__ == "__main__":
    main()
