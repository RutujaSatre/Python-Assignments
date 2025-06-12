"""Write a program which contains one class named as Arithmetic.
Arithmetic class contains two instance variable as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variables.
SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required.
After designing the above class call all instance methods by creating multiple objects. """ 


class Arithmetic:
    def __init__(self, value):
        self.value = value

    def ChkPrime(self, num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def ChkPerfect(self, num):
        return self.SumFactors(num) == num

    def Factors(self, num):
        print("Factors of",num,": ", end="")
        for i in range(1, num):
            if num % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self, num):
        factors = 0
        for i in range(1, num):
            if num % i == 0:
                factors += i
        return factors
def main():
    num = int(input("Enter number: "))

    number = Arithmetic(num)

    print("Is it prime:", number.ChkPrime(num))

    print("Is it perfect:", number.ChkPerfect(num))

    number.Factors(num)

if __name__=="__main__":
    main()
