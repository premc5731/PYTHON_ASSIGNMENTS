# 3. Create a class Book with private attribute __price. Add methods to get and set the
# price. Show encapsulation.


class Book:
    def __init__(self):
        self.price = 0

    def Get_Price(self):
        return self.price
    
    def Set_Price(self,price):
        self.price = price

def main():
    Ret = 0
    Obj = Book()
    Obj.Set_Price(1000)
    Ret = Obj.Get_Price()
    print("price of book is : ",Ret)

if __name__ == "__main__":
    main()

