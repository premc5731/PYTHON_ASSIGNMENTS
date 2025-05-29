# 3. Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
# Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.

class Numbers:
    def __init__(self,No):
        self.No = No

    def SumFactors(self):
        Sum = 0
        for i in range(1,(self.No // 2)+ 1):
            if((self.No % i) == 0):
                Sum = Sum + i
        return Sum
    
    def ChkPrime(self):
        Flag = True
        Result = Numbers.SumFactors(self)

        if Result == 1:
            Flag = True
        else:
            Flag = False

        return Flag
    def ChkPerfect(self):
        Result = Numbers.SumFactors(self)
        Flag = False

        if(Result == self.No):
            Flag = True
        else:
            Flag = False
        return Flag
    
    def Factors(self):
        for i in range(1,(self.No // 2)+1):
            if(self.No % i == 0):
                print("factor : ",i)

def main():
    Ret = False
    print("Enter a number : ",end ="")
    Value = int(input())

    Obj1 = Numbers(Value)

    Ret = Obj1.ChkPrime()
    if Ret == True:
        print(Value,"is prime number")
    else:
        print(Value,"is not a prime number")

    Ret = Obj1.ChkPerfect()
    if Ret == True:
        print(Value,"is perfect number")
    else:
        print(Value,"is not a perfect number")

    Obj1.Factors()

    Ret = Obj1.SumFactors()
    print("Summmation of factors is : ",Ret)

if __name__ == "__main__":
    main()
