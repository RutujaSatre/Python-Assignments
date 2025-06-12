# Create a class BankAccount with account_number, name, and balance. Use __init__ and create methods for deposit , withdraw, and displaying balance.

class BankAccount:

    def __init__(self,acno,name,balance):
        self.account_number = acno
        self.name = name 
        self.balance = balance

    def deposit(self,deposite):
        self.balance+=deposite
        print("Balance after deposit : ",self.balance)

    def withdraw(self,withdraw):
        self.balance -= withdraw
        print("Balance after withdraw : ",self.balance)

    def displayingBalance(self):
        print("Total balance is : ",self.balance)

    
    def display(self):
        print("Account number is : ",self.account_number)
        print("Name is : ",self.name)

        
def main():
    obj1 = BankAccount(253646,"Sumitra",235000)
    
    obj1.display()
    obj1.deposit(14565)
    obj1.withdraw(6300)
    obj1.displayingBalance()

if __name__=="__main__":
    main()