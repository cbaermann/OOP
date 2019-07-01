# class User:
#     def __init__(self):
#         self.name = 'Cody'
#         self.email = 'cody@codemail.net'
#         self.account_balance = 0
# guido.name = 'Guido'
# monty.name = 'Monty'
# guido = User()
# monty = User()
# print(guido.name)
# print(monty.name)

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email_address = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self
    


guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
cody = User('Cody Baer', 'cody@codemail.com')

guido.make_deposit(75).make_deposit(80).make_deposit(3).make_withdrawl(55).display_user_balance()
cody.make_deposit(10000).make_deposit(10).make_deposit(65).make_withdrawl(876).display_user_balance()
monty.make_deposit(100)