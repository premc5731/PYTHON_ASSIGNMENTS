# 4. Create a class Student with name, roll_no, and a class variable school_name. Print
# student details and school name. Change the school name using class name.

class Student:
    school_name = "St peters high school"
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def Display(self):
        print("Student name : ",self.name)
        print("Student roll no :",self.roll_no)

def main():
    Obj = Student("Rohan",101)
    Obj.Display()
    print("School name : ",Student.school_name)
    Student.school_name = "st maria"
    print("School name : ",Student.school_name)
    

if __name__ == "__main__":
    main()
