# 2. Write a class Rectangle with length and width. Add a method to compute area and
# perimeter.
# Area: 50, Perimeter: 30

class Rectangle:
    def __init__(self,len,wid):
        self.length = len
        self.width = wid
    
    def Area(self):
        result = 0.0
        result = self.length * self.width
        return result
    
    def Perimeter(self):
        result = 0.0
        result = 2*(self.length + self.width)
        return result
    
def main():
    ret = 0.0

    print("Enter the length : ",end = "")
    value1 = int(input())

    print("Enter the width : ",end = "")
    value2 = int(input())

    Obj1 = Rectangle(value1,value2)

    ret = Obj1.Area()
    print("Area of rectangel is : ",ret)

    ret = Obj1.Perimeter()
    print("Perimeter of rectangle is : ",ret)

if __name__ == "__main__":
    main()