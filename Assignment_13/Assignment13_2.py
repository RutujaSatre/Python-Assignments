"""Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variable as Name and Amount.
That class contains one class variable as ROI which is initialise to 10.5
Inside init method initialise all name and amount variables by accepting the values from user.
There are four instance methods inside class as Display(), Deposite(), Withdraw(), CalculateIntrest().
Deposite() method will accept the amount from user and add that value in class instance variable Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects. """ 


class BankAccount():
    ROI = 10.5

    def __init__(self,Name,Amount):
          self.Name = Name
          self.Amount = Amount

    def Deposite(self):
        Amount = int(input("Enter Deposite Amount : "))
        self.Amount +=Amount
        print(self.Amount)


    def Withdraw(self):
        value = (int(input("Enter Withdraw amount : ")))
        self.Amount -= value
        print(self.Amount)  

    def CalculateIntrest(self):
         interest = (self.Amount*BankAccount.ROI)/100
         print("Interest on amount is : ",interest ,"%")

    def Display(self):
         print("Name of Account Holder  : ",self.Name)
         print("Current Amount is : ",self.Amount)
          
def main():
        Obj1 = BankAccount(input("Enter Name : "),int(input("Enter initial Amount : ")))
        
        Obj1.Deposite()

        Obj1.Withdraw()

        Obj1.CalculateIntrest()

        Obj1.Display()
         
if __name__=="__main__":
    main()
