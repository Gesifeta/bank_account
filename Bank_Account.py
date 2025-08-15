import  uuid

class BankAccount:
    def __init__(self, customer_account, first_name, last_name, gender, initial_deposit = 0.00):
        self.account_number = customer_account
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.initial_deposit = initial_deposit
        self.balance = initial_deposit
    def deposit(self,deposit_amount):

        self.balance = float(self.balance) + deposit_amount
        return self.balance
    def withdraw(self,withdraw_amount):
        if withdraw_amount < float(self.balance) - 50:
            self.balance = float(self.balance) - withdraw_amount
            return self.balance
        else:
            return self.balance
    def account_balance(self):
        return self.balance

    





