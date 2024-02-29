import utils

if __name__ == '__main__':
    print("\n")
    account1 = utils.Account('Jack', 3000, 'abcdef68452')
    account1.show()

    account1.deposit(500, 'abcdef68452')
    account1.show()

    account_balance = account1.getBalance('abcdef68452')
    print(account_balance)
    print("\n")

    account_withdraw = account1.withdraw(2000, 'abcdef68452')
    print(account_withdraw)
    print("\n")

    account1.show()
