# 2. Write a program which contains one class named as Circle.
# Circle class contains three instance variables as radius ,area, circumference.
# That class contains one class variable as PI which is initialise to 3.14.
# Inside init method initialise all instance variables to 0.0.
# The re a re th ree in s tan ce me thod s in side cla s s a s A c cep t() , Cal cula teA rea() ,
# Calculatecircumference(), Display().
# Accept method will accept value of radius from user.
# Calculatearea() method will calculate area of Circle and store it into instance variable area.
# Calculatecircumference() method will calculate circumference of Circle and store it into instance
# variable circumference.
# And Display() method will display value of all the instance variables as radius , area,
# circumference.
# After designing the above class call all instance methods by creating multiple objects.

class Circle:
    PI = 3.14

    def __init__(self):
        self.rad = 0.0
        self.area = 0.0
        self.circ = 0.0

    def Accept(self,rad):
        self.rad = rad

    def Calculatearea(self):
        self.area = Circle.PI * self.rad * self.rad

    def Calculatecircumference(self):
        self.circ = 2 * Circle.PI * self.rad

    def Display(self):
        print("radius : ",self.rad)
        print("area : ",self.area)
        print("circumference : ",self.circ)

def main():
    Obj1 = Circle()
    Obj1.Accept(10)
    Obj1.Calculatearea()
    Obj1.Calculatecircumference()
    Obj1.Display()

    Obj2 = Circle()
    Obj2.Accept(20)
    Obj2.Calculatearea()
    Obj2.Calculatecircumference()
    Obj2.Display()


if __name__ == "__main__":
    main()