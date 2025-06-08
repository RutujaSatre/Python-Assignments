'''Write a program which contains one class named as Arithmetic.
Arithmetic class contains two instance variables as Value 1 ,Value 2.
Inside init method initialise all instance variables to 0
There are three instance method inside class as Accept(), Addition(), Subtraction(),Multiplication(),Division().
Accept() method will accept value of Value1 and Value2 from user .
Addition() method will perform addition of Value1,Value2 and return result.
Subtraction() method will perform subtraction of Value1,Value2 and return result.
Multiplication() method will perform Multiplication of Value1,Value2 and return result.
Division() method will perform division of Value1,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.
'''


class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter First Value : ")
        self.Value1 = int(input())

        print("Enter Second Value : ")
        self.Value2 = int(input())

    def Addition(self):
        print("Addition is : ",self.Value1+self.Value2)

    def Subtraction(self):
        print("Subtraction is : ",self.Value1-self.Value2)

    def Multiplication(self):
        print("Multiplication is : ",self.Value1*self.Value2)

    def Division(self):
        print("Division is : ",self.Value1/self.Value2)

def main():
    Obj1 = Arithmetic()

    Obj1.Accept()
    Obj1.Addition()
    Obj1.Subtraction()
    Obj1.Multiplication()
    Obj1.Division()


if __name__=="__main__":
    main()