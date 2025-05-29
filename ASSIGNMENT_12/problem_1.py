# 1.Write a program which contains one class named as Demo.
# Demo class contains two instance variables as no1 ,no2.
# That class contains one class variable as Value.
# There are two instance methods of class as Fun and Gun which displays values of instance
# variables.
# Initialise instance variable in init method by accepting the values from user.
# After creating the class create the two objects of Demo class as
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)
# Now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()


class Demo:
    Value = "Class Variable"
    def __init__ (self,item1,item2):
        self.No1 = item1
        self.No2 = item2

    def Fun(self):
        print("Inside Fun No1 : ",self.No1)
        print("Inside Fun No2 : ",self.No2)

    def Gun(self):
        print("Inside Gun No1 : ",self.No1)
        print("Inside Gun No2 : ",self.No2)

def main():
    print("Enter first number : ",end = "")
    Value1 = int(input())

    print("Enter second number : ",end = "")
    Value2 = int(input())

    print("Enter third number : ",end = "")
    Value3 = int(input())

    print("Enter fourth number : ",end = "")
    Value4 = int(input())

    Obj1 = Demo(Value1,Value2)
    Obj2 = Demo(Value3,Value4)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()
