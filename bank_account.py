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
guido = BankAccount('Guido')
guido.deposit(100).deposit(100).deposit(50).withdrawl(100).yield_interest().display_account_info()
mario = BankAccount('Mario')
mario.deposit(50).deposit(100).withdrawl(50).withdrawl(10).withdrawl(10).withdrawl(10).yield_interest().display_account_info()


