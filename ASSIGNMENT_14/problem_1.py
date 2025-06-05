# 1. Create a class Employee with attributes name, emp_id, and salary. Create objects
# of this class and print their details using a method.
# Expected Output:
# name: Rohit, iD: 101, salary: 50000

class Employee:
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary

    def Display(self):
        print("name   : ",self.name)
        print("id     : ",self.id)
        print("salary : ",self.salary)

def main():
    Obj1 = Employee("Rohit",101,50000)
    Obj1.Display()

if __name__ == "__main__":
    main()