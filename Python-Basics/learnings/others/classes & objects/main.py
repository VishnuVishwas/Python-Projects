# Bank System using oops 

# Parent class = user()
    # Holds the details of user
    # has function to show user deatils 
# Child class = bank()
    # Stores details about account balance
    # Stores details about amount
    # Allows for deposite, withdraw, view_balance

# parent class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")
        print("")
        print("Name : ", self.name)
        print("age : ", self.age)
        print("gender : ", self.gender)

# child class 
class Bank(User):
    def __init__(self, name, age, gender) :
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print("Amount credited successfully.\nBalance: Rs. ", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= self.amount
            print("Balance : Rs. ", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance Rs. ", self.balance)

if __name__ == "__main__":
    vishnu = Bank('Vishnu', 20, "male")
    vishnu.deposit(1000)
    vishnu.withdraw(500)
    vishnu.view_balance()
