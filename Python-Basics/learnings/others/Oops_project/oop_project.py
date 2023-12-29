from bank_account import *

Vishnu = BankAccount(1000, "vishnu")
Sara = BankAccount(2000, "sara")

Vishnu.getBalance()
Sara.getBalance()

Sara.deposit(500)

Vishnu.withdraw(100000)
Vishnu.withdraw(100)

Vishnu.transfer(109000, Sara)
Vishnu.transfer(500, Sara)

Jim = InterestRewardsAcct(1000, 'Jim')
Jim.deposit(100)
Jim.transfer(100, Vishnu)

gojo = SavingsAcccount(1000, 'Gojo')
gojo.deposit(100)
gojo.transfer(1000, Vishnu)
