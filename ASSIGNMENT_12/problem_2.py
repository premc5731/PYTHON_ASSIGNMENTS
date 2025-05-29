# 2. Write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius ,Area, Circumference.
# That class contains one class variable as PI which is initialise to 3.14.
# Inside init method initialise all instance variables to 0.0.
# The re a re th ree in s tan ce me thod s in side cla s s a s A c cep t() , Cal cula teA rea() ,
# CalculateCircumference(), Display().
# Accept method will accept value of Radius from user.
# CalculateArea() method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference() method will calculate circumference of circle and store it into instance
# variable Circumference.
# And Display() method will display value of all the instance variables as Radius , Area,
# Circumference.
# After designing the above class call all instance methods by creating multiple objects.

class Circle:
    PI = 3.14

    def __init__(self):
        self.Rad = 0.0
        self.Area = 0.0
        self.Circ = 0.0

    def Accept(self,Rad):
        self.Rad = Rad

    def CalculateArea(self):
        self.Area = Circle.PI * self.Rad * self.Rad

    def CalculateCircumference(self):
        self.Circ = 2 * Circle.PI * self.Rad

    def Display(self):
        print("Radius : ",self.Rad)
        print("Area : ",self.Area)
        print("Circumference : ",self.Circ)

def main():
    Obj1 = Circle()
    Obj1.Accept(10)
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

    Obj2 = Circle()
    Obj2.Accept(20)
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()


if __name__ == "__main__":
    main()