# Create a class Calculator with methods for add, subtract, multiply, divide. Ask user input for values and call methods accordingly.

class Calculator:
    
    def __init__(self , value1 , value2):
        self.value1 = value1
        self.value2 = value2

    def Add(self):
        print("Addition is : ",self.value1 + self.value2)

    def Subtract(self):
        print("Subtraction is : ",self.value1 - self.value2)

    def Multiply(self):
        print("Multiplication is : ",self.value1 * self.value2)

    def divide(self):
        print("Division is : ",self.value1 / self.value2)


def main():
    Obj = Calculator(int(input("Enter first number : ")),int(input("Enter Second number : ")))

    Obj.Add()
    Obj.Subtract()
    Obj.Multiply()
    Obj.divide()
   

if __name__=="__main__":
    main()