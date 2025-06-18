# 10. Demonstrate private, protected and public access modifiers using a class Employee
# with attributes: __salary, _department, name.

class Employee:
    def __init__(self,name,dep,sal):
        self.name = name
        self._department = dep
        self.__salary = sal

class Person(Employee):
    def __init__(self,name,dep,sal):
        super().__init__(name,dep,sal)
    
    def Display(self):
        print("Inside Person class : ")
        print("Name        : ",self.name)
        print("Department  : ",self._department)
        # print("Salary  : ",self.__salary)   # it is private u cant access outside of class

def main():
    Obj = Person("Rahul","CS",10000)
    Obj.Display()

if __name__ == "__main__":
    main()