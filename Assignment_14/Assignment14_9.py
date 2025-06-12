# Create a class Product with attributes name and price .Implement __eq__ method to compare two products if they are equal in price.

class Product:

    def __init__(self , Name , Price):
        self.name = Name
        self.price = Price

    def __eq__(self,value):
        if isinstance(value,Product):
            return self.price == value.price
        return False

def main():
    obj1 = Product("Laptop",50000)
    obj2 = Product("mobile",15000)
    obj3 = Product("bike",50000)

    print(obj1 == obj2)
    print(obj1 == obj3)

if __name__=="__main__":
    main()