def ChkPrime(no):
    flag = True
    for i in range(2,((no//2) + 1)):
        if no % i == 0:
            flag = False
            break
    
    return flag
