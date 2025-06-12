# Create a class Employee with attribute name, emp_id , and salary. Create objects of this class and print their details using a method.

class Employee:
    
    def __init__(self,Name,id,salary):
        self.Name = Name
        self.emp_id = id
        self.Salary = salary

    def DisplayDetails(self):
        print("Employee Name : ",self.Name , " , Employee ID : ",self.emp_id , " , Employee Salary : ",self.Salary)

def main():
        Obj1 = Employee("Rutuja",101,120000)
        Obj2 = Employee("Purva",102,150000)

        Obj1.DisplayDetails()
        Obj2.DisplayDetails()

if __name__=="__main__":
    main()