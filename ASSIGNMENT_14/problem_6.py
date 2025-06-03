# 6. Create a class Calculator with methods for add, subtract, multiply, divide. Ask user
# input for values and call methods accordingly.

class Calculator:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        self.ans = 0

    def Accept(self,No1,No2):
        self.value1 = No1
        self.value2 = No2
        

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

    Obj1 = Calculator()
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
