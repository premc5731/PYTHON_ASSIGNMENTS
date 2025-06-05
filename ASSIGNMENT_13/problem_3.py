# 3. Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as value.
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
    def __init__(self,no):
        self.no = no

    def SumFactors(self):
        sum = 0
        for i in range(1,(self.no // 2)+ 1):
            if((self.no % i) == 0):
                sum = sum + i
        return sum
    
    def ChkPrime(self):
        flag = True
        result = Numbers.SumFactors(self)

        if result == 1:
            flag = True
        else:
            flag = False

        return flag
    def ChkPerfect(self):
        result = Numbers.SumFactors(self)
        flag = False

        if(result == self.no):
            flag = True
        else:
            flag = False
        return flag
    
    def Factors(self):
        for i in range(1,(self.no // 2)+1):
            if(self.no % i == 0):
                print("factor : ",i)

def main():
    ret = False
    print("Enter a number : ",end ="")
    value = int(input())

    Obj1 = Numbers(value)

    ret = Obj1.ChkPrime()
    if ret == True:
        print(value,"is prime number")
    else:
        print(value,"is not a prime number")

    ret = Obj1.ChkPerfect()
    if ret == True:
        print(value,"is perfect number")
    else:
        print(value,"is not a perfect number")

    Obj1.Factors()

    ret = Obj1.SumFactors()
    print("summmation of factors is : ",ret)

if __name__ == "__main__":
    main()
