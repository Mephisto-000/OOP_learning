"""
模擬銀行營運

操作需求 :
        1. 建立帳戶
        2. 存款
        3. 提款
        4. 查看餘額

資料需求 :
        1. 顧客姓名 : name
        2. 密碼 : password
        3. 餘額 : balance

"""


class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None

        if amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None

        self.balance = self.balance + amountToDeposit
        return self.balance

    def withdraw(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None

        if amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None

        if amountToDeposit > self.balance:
            print('You cannot withdraw more than you have in your account')
            return None

        self.balance = self.balance - amountToDeposit
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        return self.balance

    def show(self):
        print('     Name: ', self.name)
        print('     Balance: ', self.balance)
        print('     Password: ', self.password)
        print("\n")
