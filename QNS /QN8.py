class AccountHolder:
    def __init__ (self, name, age, address):
        self.name = name 
        self.age = age 
        self.address = address

class LoanAccount(AccountHolder):
    def __init__ (self, name, age, address, loan_amount, interest_rate):
        super().__init__ (name, age, address)
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate

    def apply_for_loan(self,amount):
        if amount > 0:
            self.loan_amount += amount
            print (f'{self.name} has applied for a loan of ${amount}.')

        else:
            print(f'INVALID AMOUNT!!')

    def repay_loan(self, amount):
        if amount <= 0:
            print(f'INVALID REPAYMENT AMOUNT!!')
        elif amount > self.loan_amount:
            print(f'You cannot repay more than the loan amount!!')
        else:
            self.loan_amount -= amount
            print(f'{self.name} has repaid ${amount}.')

    def display_info(self):
        print(f'Name: {self.name}\nBalance:{self.loan_amount}')


Cust1 = LoanAccount('Sarah', 34, 'Mukono', 600, 0.08)

Cust1.apply_for_loan(200)
Cust1.repay_loan(150)
Cust1.display_info()  