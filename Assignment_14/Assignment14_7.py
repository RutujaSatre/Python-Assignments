# Create a base class Person with name and age. Derive a class Teacher with subject and salary .Use super() to call base class constructor and print both.


class Person:

    def __init__(self , Name , Age):
        self.name = Name
        self.age = Age        

class Teacher(Person):

    def Display(self , subject , salary):
        self.subject = subject
        self.salary = salary

        super().__init__(self.name,self.age)
        print("Subject of Teacher : ",self.subject)
        print("Salary of Teacher : ",self.salary)
        print("Name of Person: " ,self.name)
        print("Age of Person : ",self.age)

def main():
    Obj1 = Teacher("Rutuja",20)
    Obj1.Display("Python",45000)

if __name__=="__main__":
    main()
    