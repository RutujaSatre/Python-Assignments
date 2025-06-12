# Create a class Student with name, roll_no and a class variable school_name. Print student details and school name . Change the school name using class name.

class Student:
    school_name = "Integrated"

    def __init__(self,name,rollno):
        self.Name = name 
        self.roll_no = rollno

    def StudentDetails(self):
        print("Name : ",self.Name)
        print("Roll no : ",self.roll_no)

    def School(self):
        print("School Name is : ",Student.school_name)
        Student.school_name =input("Enter new school name is : ")
        print("The current School name is : ",Student.school_name)
               
def main():
    Obj1 = Student("Apurva ",12)
    Obj1.StudentDetails()
    Obj1.School()

if __name__=="__main__":
    main()

    