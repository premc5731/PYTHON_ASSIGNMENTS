# 1.Write a program which contains one class named as Demo.
# Demo class contains two instance variables as no1 ,no2.
# That class contains one class variable as value.
# There are two instance methods of class as Fun and Gun which displays values of instance
# variables.
# Initialise instance variable in init method by accepting the values from user.
# After creating the class create the two objects of Demo class as
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)
# now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()


class Demo:
    value = "Class Variable"
    def __init__ (self,item1,item2):
        self.no1 = item1
        self.no2 = item2

    def Fun(self):
        print("Inside Fun no1 : ",self.no1)
        print("Inside Fun no2 : ",self.no2)

    def Gun(self):
        print("Inside Gun no1 : ",self.no1)
        print("Inside Gun no2 : ",self.no2)

def main():
    print("Enter first number : ",end = "")
    value1 = int(input())

    print("Enter second number : ",end = "")
    value2 = int(input())

    print("Enter third number : ",end = "")
    value3 = int(input())

    print("Enter fourth number : ",end = "")
    value4 = int(input())

    Obj1 = Demo(value1,value2)
    Obj2 = Demo(value3,value4)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()
