class Bank:
    bankname = "Union"
    branch = "A23,BBSR,India"

    def __init__(self, username, pan, address):
        self.username = username
        self.pan = pan
        self.address = address
        self.balance = 0.0  # set account balance to 0.0
        print(f'Hello {self.username} cong! your account created successfully ')

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'{amount} deposited successfully')

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            print(f'{amount} withdraw successfully')
        else:
            print('Insufficient Fund')

    def ministatement(self):
        print(f'Your account balance is {self.balance}')


print(f'Welcome to {Bank.bankname} , {Bank.branch}')

username = input('Enter Your name :')
pan = input('Enter PAN card number : ')
address = input('Enter Your address : ')

b = Bank(username, pan, address)  # object creation based on user provided data

while True:
    print('\nPlease Select any Option : ')
    print('1.Deposit\n2.Withdraw\n3.Ministatement\n4.Stop')
    option = int(input(' '))

    if option == 1:
        amount = float(input('Enter Deposited amount : '))
        b.deposit(amount)

    elif option == 2:
        amount = float(input('Enter Withdraw amount : '))
        b.withdraw(amount)

    elif option == 3:
        b.ministatement()

    elif option == 4:
        print('Thanks for using Union Bank ')
        break
    else:
        print('Invalid Option. please select a  valid option')
