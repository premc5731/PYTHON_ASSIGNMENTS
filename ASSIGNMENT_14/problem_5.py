# 5. Create a class BankAccount with account_number, name, and balance. Use
# __init__ and create methods for deposit, withdraw, and displaying balance.

class BankAccount:
    def __init__(self,name,bal):
        self.name = name
        self.balance = bal

    def Deposit(self,bal):
        self.balance += bal
        print("Deposite sucessfull")

    def Withdraw(self,bal):
        if( bal <= self.balance):
            self.balance -= bal
            print("Withdraw sucessfull")
        else:
            print("Insuffient balance ")

    def Display(self):
        print("Account holder name : ",self.name)
        print("Balance             : ",self.balance)

def main():
    Obj1 = BankAccount("Ravi",10000)
    Obj1.Deposit(500)
    Obj1.Withdraw(1000)
    Obj1.Display()

if __name__ == "__main__":
    main()
