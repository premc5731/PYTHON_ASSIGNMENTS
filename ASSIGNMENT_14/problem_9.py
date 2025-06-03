# 9. Create a class Product with attributes name and price. Implement __eq__ method
# to compare two products if they are equal in price.


class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __eq__(self,other):
        flag = False
        if isinstance(self,Product):
            if self.price == other.price:
                flag = True
        return flag
    
def main():
    Ret = False
    Obj1 = Product("Oppo",10000)
    Obj2 = Product("Vivo",10000)
    Obj3 = Product("Oppo",20000)
    Obj4 = Product("Oppo",10000)

    Ret = Obj1.__eq__(Obj2)
    print(Ret)              # True
    print(Obj1 == Obj2)    # True ( u can write in this way also since u have overidden == in __eq__ method now it will check only price of both objects)

    Ret = Obj1.__eq__(Obj3)
    print(Ret)              # False

    Ret = Obj2.__eq__(Obj3)
    print(Ret)              # False

    print(Obj1 == Obj4)   # False (without __eq__)
    # because == will check for user defined datatypes and it will check value for built in datatypes like for int,string,list etc



if __name__ == "__main__":
    main()