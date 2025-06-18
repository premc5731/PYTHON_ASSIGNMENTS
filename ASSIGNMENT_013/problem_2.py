# 2. Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as name & amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
# CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable
# amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount
# from class instance variable amount.
# CalculateIntrest() method calculate the interest based on amount by considering rate of interest
# which is Class variable as ROI.
# And Display() method will display value of all the instance variables as name and amount.
# After designing the above class call all instance methods by creating multiple objects.

class BankAccount:
    ROI = 10.5
    def __init__(self,name,amt):
        self.name = name
        self.amount = amt
        self.interest = 0.0

    def Deposit(self,amt):
        self.amount += amt
        print("Deposite sucessfull")

    def Withdraw(self,amt):
        if( amt <= self.amount):
            self.amount -= amt
            print("Withdraw sucessfull")
        else:
            print("Insuffient balance ")

    def CalculateIntrest(self):
        self.interest = ((BankAccount.ROI / 100)* self.amount)

    def Display(self):
        print("Account holder name : ",self.name)
        print("Balance             : ",self.amount)
        print("interest amount     : ",self.interest)

def main():
    Obj1 = BankAccount("Ravi",10000)
    Obj1.Deposit(500)
    Obj1.Withdraw(1000)
    Obj1.CalculateIntrest()
    Obj1.Display()

if __name__ == "__main__":
    main()
