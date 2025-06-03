# 3. Create a class Book with private attribute __price. Add methods to get and set the
# price. Show encapsulation.


class Book:
    def __init__(self):
        self.Price = 0

    def Get_Price(self):
        return self.Price
    
    def Set_Price(self,price):
        self.Price = price

def main():
    Ret = 0
    Obj = Book()
    Obj.Set_Price(1000)
    Ret = Obj.Get_Price()
    print("Price of book is : ",Ret)

if __name__ == "__main__":
    main()

