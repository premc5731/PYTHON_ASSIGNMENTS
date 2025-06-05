# 3. Write a program which contains one class named as Arithmetic.
# Arithmetic class contains three instance variables as value1 ,value2.
# Inside init method initialise all instance variables to 0.
# There are three instance methods inside class as Accept(), Addition(), Subtraction(),
# Multiplication(), Division().
# Accept method will accept value of value1 and value2 from user.
# Addition() method will perform addition of value1 ,value2 and return result.
# Subtraction() method will perform subtraction of value1 ,value2 and return result.
# Multiplication() method will perform multiplication of value1 ,value2 and return result.
# Division() method will perform division of value1 ,value2 and return result.
# After designing the above class call all instance methods by creating multiple objects.

class Arithemetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        self.ans = 0

    def Accept(self,no1,no2):
        self.value1 = no1
        self.value2 = no2
        

    def Addition(self):
        self.ans = 0
        self.ans = self.value1 + self.value2
        return self.ans
    
    def Subraction(self):
        self.ans = 0
        self.ans = self.value1 - self.value2
        return self.ans
    
    def Multiplication(self):
        self.ans = 0
        self.ans = self.value1 * self.value2
        return self.ans
    
    def Division(self):
        self.ans = 0
        try:
            self.ans = self.value1 // self.value2
            return self.ans
        except ZeroDivisionError:
            print("Invalid input")

        
def main():
    result = 0
    print("Enter first number : ",end = "")
    record1 = int(input())

    print("Enter second number : ",end = "")
    record2 = int(input())

    Obj1 = Arithemetic()
    Obj1.Accept(record1,record2)

    result = Obj1.Addition()
    print("Addition is : ",result)

    result = Obj1.Subraction()
    print("Subraction is : ",result)

    result = Obj1.Multiplication()
    print("Multiplication is : ",result)

    result = Obj1.Division()
    print("Division is : ",result)

if __name__ == "__main__":
    main()