# Write a class Rectangle with length and width. Add methods to compute area and perimeter.

class Rectangle :

    def __init__(self,Length,Width):
        self.length = Length
        self.width = Width

    def Calculate(self):
        Area = self.length*self.width
        Perimeter = (self.length+self.width)*2

        print("Area : ",Area,"Perimeter : ",Perimeter)

def main():
    Obj1 = Rectangle(10,12)
    Obj1.Calculate() 

    Obj2 = Rectangle(9,14)
    Obj2.Calculate()


if __name__== "__main__":
    main()
