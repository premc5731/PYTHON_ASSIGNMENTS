# 6. sum of First N Natural Numbers
# Write a recursive function to calculate sum from 1 to n.
# sum_n(5) → 15

sum = 0
icnt = 1

def SumN(No):
    global sum, icnt

    if(icnt <= No):
        sum = sum + icnt
        icnt += 1
        SumN(No)

    return sum


def main():
    result = SumN(5)
    print("sum of natural numbers is : ",result)

if __name__ == "__main__":
    main()