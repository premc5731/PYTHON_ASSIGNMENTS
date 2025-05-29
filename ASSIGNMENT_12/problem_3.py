# 3. Write a program which contains one class named as Arithmetic.
# Arithmetic class contains three instance variables as Value1 ,Value2.
# Inside init method initialise all instance variables to 0.
# There are three instance methods inside class as Accept(), Addition(), Subtraction(),
# Multiplication(), Division().
# Accept method will accept value of Value1 and Value2 from user.
# Addition() method will perform addition of Value1 ,Value2 and return result.
# Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
# Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
# Division() method will perform division of Value1 ,Value2 and return result.
# After designing the above class call all instance methods by creating multiple objects.

class Arithemetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
        self.Ans = 0

    def Accept(self,No1,No2):
        self.Value1 = No1
        self.Value2 = No2
        

    def Addition(self):
        self.Ans = 0
        self.Ans = self.Value1 + self.Value2
        return self.Ans
    
    def Subraction(self):
        self.Ans = 0
        self.Ans = self.Value1 - self.Value2
        return self.Ans
    
    def Multiplication(self):
        self.Ans = 0
        self.Ans = self.Value1 * self.Value2
        return self.Ans
    
    def Division(self):
        self.Ans = 0
        try:
            self.Ans = self.Value1 // self.Value2
            return self.Ans
        except ZeroDivisionError:
            print("Invalid input")

        
def main():
    Result = 0
    print("Enter first number : ",end = "")
    Record1 = int(input())

    print("Enter second number : ",end = "")
    Record2 = int(input())

    Obj1 = Arithemetic()
    Obj1.Accept(Record1,Record2)

    Result = Obj1.Addition()
    print("Addition is : ",Result)

    Result = Obj1.Subraction()
    print("Subraction is : ",Result)

    Result = Obj1.Multiplication()
    print("Multiplication is : ",Result)

    Result = Obj1.Division()
    print("Division is : ",Result)

if __name__ == "__main__":
    main()