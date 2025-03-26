class BankAccount:
    def __init__ (self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

class SavingsAccount(BankAccount):
    def __init__ (self, account_number, balance, account_holder, interest_rate):
        super().__init__(account_number,balance,account_holder)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount 
            print(f'Deposited ${amount}\nNew balance: ${self.balance}')
        else:
            print('INVALID AMOUNT!!!')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount 
            print (f'Withdrawn: ${amount}\nNew balance: ${self.balance}')
        else:
            print('THAT AMOUNT DOEES NOT EXIST IN YOUR ACCOUNT!!!')

    def display_info(self):
        print(f'Account Number: {self.account_number}\nAccount name: {self.account_holder}\nBalance: {self.balance}')


Acc1 = SavingsAccount(3087689, 2000, 'Denise', 0.5)
Acc2 = SavingsAccount(457690, 100, 'Isaac', 0.5)

Acc1.deposit(200)
Acc2.withdraw(20000)

Acc1.display_info()
