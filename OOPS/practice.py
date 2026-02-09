from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self,accountNumber,holderName,balance=0):
        self.accountNumber=accountNumber
        self.holderName=holderName
        self.balance=balance
    
    @abstractmethod
    def deposit(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass
    
    def display_details(self):
        print(f"Account Number={self.accountNumber}")
        print(f"Account Holder Name={self.holderName}")

class SavingsAccount(BankAccount):

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Amount deposited successfully!")
    
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")
    
    def get_balance(self):
        print(f"Your balance is : {self.balance}")
    
class CurrentAccount(BankAccount):

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Amount deposited successfully!")
    
    def withdraw(self,amount):
        if amount<50000:
            self.balance=self.balance-amount
            print("Amount withdrawn successfully!")
        else:
            print("Limit Exceeded!")
    
    def get_balance(self):
        print(f"Your balance is : {self.balance}")


flag=True
while(flag):
    print("press 1 for current account, 2 for savings account or 3 to exit")
    actype=int(input("Enter choice"))
    if actype==1:
        accountnumber=int(input("Enter account number: "))
        name=input("Enter account holder name:")
        account=CurrentAccount(accountnumber,name)
    if actype==2:
        accountnumber=int(input("Enter account number: "))
        name=input("Enter account holder name:")
        account=SavingsAccount(accountnumber,name)
    if actype==3:
        flag=False
        break

    while True:
        print("Press 1 for withdrawl")
        print("Press 2 for deposit")
        print("press 3 to check balance")
        print("press 4 to print account details")
        print("press 5 to exit to main menu")

        choice=int(input("Enter choice"))

        if choice==1:
            amount=int(input("Enter Amount"))
            account.withdraw(amount)
        elif choice==2:
            amount=int(input("Enter Amount"))
            account.deposit(amount)
        elif choice==3:
            account.get_balance()
        elif choice==4:
            account.display_details()
        elif choice==5:
            break
        else:
            print("Wrong choice, try again!")