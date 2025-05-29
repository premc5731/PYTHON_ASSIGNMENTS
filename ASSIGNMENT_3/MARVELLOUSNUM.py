def ChkPrime(No):
    Flag = True
    for i in range(2,((No//2) + 1)):
        if No % i == 0:
            Flag = False
            break
    
    return Flag
