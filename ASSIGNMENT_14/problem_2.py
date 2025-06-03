# 2. Write a class Rectangle with length and width. Add a method to compute area and
# perimeter.
# Area: 50, Perimeter: 30

class Rectangle:
    def __init__(self,Len,Wid):
        self.Length = Len
        self.Width = Wid
    
    def Area(self):
        Result = 0.0
        Result = self.Length * self.Width
        return Result
    
    def Perimeter(self):
        Result = 0.0
        Result = 2*(self.Length + self.Width)
        return Result
    
def main():
    Ret = 0.0

    print("Enter the length : ",end = "")
    Value1 = int(input())

    print("Enter the width : ",end = "")
    Value2 = int(input())

    Obj1 = Rectangle(Value1,Value2)

    Ret = Obj1.Area()
    print("Area of rectangel is : ",Ret)

    Ret = Obj1.Perimeter()
    print("Perimeter of rectangle is : ",Ret)

if __name__ == "__main__":
    main()