from models.user import User

# child class 
class Bank(User):
    def __init__(self, name, age, gender) :
        super().__init__(name, age, gender)
        self.balance = 0

    # deposit amount
    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print("Amount credited successfully.\nBalance: Rs. ", self.balance)

    # withdraw amount
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= self.amount
            print("Balance : Rs. ", self.balance)

    # view balance 
    def view_balance(self):
        self.show_details()
        print("Account balance Rs. ", self.balance)