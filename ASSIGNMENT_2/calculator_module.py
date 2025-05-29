def Add(No1,No2):
    Ans = No1 + No2
    return Ans

def Sub(No1,No2):
    Ans = No1 - No2
    return Ans

def Mult(No1,No2):
    Ans = No1 * No2
    return Ans

def Div(No1,No2):
    try:    
        Ans = No1 / No2
    except(ArithmeticError):
        print("Arithemetic error")
    return Ans

