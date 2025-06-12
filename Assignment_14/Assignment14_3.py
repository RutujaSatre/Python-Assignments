# Create a class Book with private attribute __price. Add method to get and set the price.Show encapsulation.

class Book:

    def __init__(self,title,price):
        self.title = title
        self.__price = price

    def getPrice(self):
        return self.__price

    def setPrice(self,newPrice):
        if newPrice>=0:
            self.__price = newPrice

        else:
            print("Price must be Positive ")

        print("Book Name : ",self.title)
        print("Price is : ",self.__price)

def main():
    Obj = Book("Python Programming",500)
    Obj.getPrice()
    Obj.setPrice(600)


if __name__=="__main__":
    main()