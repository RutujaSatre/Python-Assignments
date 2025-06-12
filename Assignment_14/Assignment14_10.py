# Demonstrate private , protected and public access modifiers using a class Employee with attributes: __salary,_department, name .

class Employee:

    def __init__(self , name , department , salary):
        self.name = name
        self._department = department
        self.__salary = salary

    def modifier(self):
        print("Name : ",self.name)
        print("Department : ",self._department) 
        print("Salary : ",self.__salary)
        

def main():
    obj = Employee("Nimish","Technical",200000)
    obj.modifier()

if __name__=="__main__":
    main()