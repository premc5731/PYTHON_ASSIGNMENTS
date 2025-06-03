# 7. Create a base class Person with name and age. Derive a class Teacher with subject
# and salary. Use super() to call base class constructor and print both.


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self,name,age,sub,sal):
        super().__init__(name,age)
        self.subject = sub
        self.salary = sal

    def Display(self):
        print("Name    : ",self.name)
        print("Age     : ",self.age)
        print("Subject : ",self.subject)
        print("Salary  : ",self.salary)

def main():
    Obj = Teacher("Rahul",35,"Maths",25000)
    Obj.Display()

if __name__ == "__main__":
    main()