# 2. Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
# CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable
# Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount
# from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
# which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.

class BankAccount:
    ROI = 10.5
    def __init__(self,Name,Amt):
        self.Name = Name
        self.Amount = Amt
        self.Interest = 0.0

    def Deposit(self,Amt):
        self.Amount += Amt
        print("Deposite sucessfull")

    def Withdraw(self,Amt):
        if( Amt <= self.Amount):
            self.Amount -= Amt
            print("Withdraw sucessfull")
        else:
            print("Insuffient balance ")

    def CalculateIntrest(self):
        self.Interest = ((BankAccount.ROI / 100)* self.Amount)

    def Display(self):
        print("Account holder name : ",self.Name)
        print("Balance             : ",self.Amount)
        print("Interest amount     : ",self.Interest)

def main():
    Obj1 = BankAccount("Ravi",10000)
    Obj1.Deposit(500)
    Obj1.Withdraw(1000)
    Obj1.CalculateIntrest()
    Obj1.Display()

if __name__ == "__main__":
    main()
