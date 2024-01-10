# Bank System using oops 

# Parent class = user()
    # Holds the details of user
    # has function to show user deatils 
# Child class = bank()
    # Stores details about account balance
    # Stores details about amount
    # Allows for deposite, withdraw, view_balance

from models.bank import Bank

if __name__ == "__main__":
    vishnu = Bank('Vishnu', 20, "male")
    vishnu.deposit(1000)
    vishnu.withdraw(500)
    vishnu.view_balance()

    vishwas = Bank('vishwas', 20, "male")
    vishwas.deposit(700)
    vishwas.withdraw(500)
    vishwas.view_balance()
