# 1. Create a class Employee with attributes name, emp_id, and salary. Create objects
# of this class and print their details using a method.
# Expected Output:
# Name: Rohit, ID: 101, Salary: 50000

class Employee:
    def __init__(self,Name,Id,Salary):
        self.Name = Name
        self.Id = Id
        self.Salary = Salary

    def Display(self):
        print("Name   : ",self.Name)
        print("Id     : ",self.Id)
        print("Salary : ",self.Salary)

def main():
    Obj1 = Employee("Rohit",101,50000)
    Obj1.Display()

if __name__ == "__main__":
    main()