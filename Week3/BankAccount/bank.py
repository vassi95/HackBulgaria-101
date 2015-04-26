

class BankAccount:

    def __init__(self, name, amount, currency):
        self.name = name
        self.amount = amount
        self.currency = currency
        self.__history = ["Account was created"]

    def __str__(self):
        message = "Bank account for {} with balance of {}{}"
        return message.format(self.name, self.amount, self.currency)

    def __int__(self):
        self.__history.append('__int__ check -> {}{}'.format(
            self.amount, self.currency))
        return self.balance()

    def deposit(self, money):
        if money < 0:
            raise ValueError
        else:
            self.amount += money
            self.__history.append('Deposited {}{}'.format(money, self.currency))

    def balance(self):
        self.__history.append("Balance -> {}{}".format(self.amount, self.currency))
        return self.amount

    def withdraw(self, money):
        if self.amount < money:
            raise ValueError
            self.__history.append("Withdraw for {}{} failed".format(
                self.amount, self.currency))
        else:
            self.amount -= money
            self.__history.append("{}{} was withdrawn".format(
                money, self.currency))
            return True

    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            raise ValueError
        else:
            self.withdraw(amount)
            account.deposit(amount)
            self.__history.append("Transfer to {} for {}{}".format(
                account.name, amount, self.currency))
        return True

    def history(self):
        return self.__history


if __name__ == '__main__':
    account = BankAccount("Rado", 0, "$")
    print(account)
    account.deposit(1000)
    print(account.balance())
    print(str(account))
    print(int(account))
    print(account.history())
    print(account.withdraw(500))
    print(account.balance())
    print(account.history())
    print(account.withdraw(1000))
    print(account.balance())
    print(account.history())
    rado = BankAccount("Rado", 1000, "$")
    ivo = BankAccount("Ivo", 0, "$")
    print(rado.transfer_to(ivo, 500))
    print(rado.balance())
    print(ivo.balance())
    print(rado.history())
    print(ivo.history())
