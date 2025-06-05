# 4. Power Function Using Recursion
# Write a recursive function to calculate x^n.
# power(2, 3) → 8


icnt = 1
result = 1

def Power(X,N):
    global icnt,result

    # while(icnt <= N):
    #     result= result * X
    #     icnt += 1

    if(icnt <= N):
        result= result * X
        icnt += 1
        Power(X,N)

    return result
def main():
    result = Power(2,3)
    print("result : ",result)

if __name__ == "__main__":
    main()