class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email_address = email_address
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrawl(self, amount):
        self.balance -= amount
        return self
    
    def ddisplay_account_info(self):
        print(self.name, self.balance)
        return self

class BankAccount:
    def __init__(self, username, int_rate= '', balance= ''):
        self.name = username
        self.int_rate = .001
        self.balance = 0
    
    def deposit(self,amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f'Balance:${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance +(self.balance * self.int_rate)
        return self

guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
cody = User('Cody Baer', 'cody@codemail.com')
guido = BankAccount('Guido')
cody = BankAccount('Cody')
# guido.deposit(100).display_account_info()
# guido.deposit(100).withdrawl(10).yield_interest().display_account_info()
cody.deposit(100).withdrawl(150).yield_interest().display_account_info()