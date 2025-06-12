# Create a class Vehicle with method start(). Derive class Car and override the method start() with additional behaviour. Show method overriding.

class Vehicle : 

    def start(self):
        print("Vehicle is start")


class Car(Vehicle) : 

    def start(self):
        print("Car is start")

def main():
    Obj = Car()
    Obj.start()

if __name__=="__main__":
    main()