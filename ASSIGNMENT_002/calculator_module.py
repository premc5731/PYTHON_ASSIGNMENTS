def Add(no1,no2):
    ans = no1 + no2
    return ans

def Sub(no1,no2):
    ans = no1 - no2
    return ans

def Mult(no1,no2):
    ans = no1 * no2
    return ans

def Div(no1,no2):
    try:    
        ans = no1 / no2
    except(ArithmeticError):
        print("Arithemetic error")
    return ans

