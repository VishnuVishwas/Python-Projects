# Bank Account Management System

class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, intitalAmount, acctName):
        self.balance = intitalAmount
        self.name = acctName
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}"
        )

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Desposite complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWith draw complete")    
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print("\n******\n\nBeginning Transfer..")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete!\n\n******")
        except BalanceException as error:
            print(f"\nTransfer interrupted. {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("Deposit Complete")
        self.getBalance()

class SavingsAcccount(InterestRewardsAcct):
    def __int__(self, intitalAmount, acctName):
        super().__init__(intitalAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + 5)
            self.balance = self.balance - (amount + 5)
            print("Withdraw Completed..")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted {error}")