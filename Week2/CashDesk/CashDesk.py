class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        return "\n{} $ bills".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __getitem__(self, index):
        return self.bills[index]

    def __len__(self):
        return len(self.bills)

    def total(self, bills):
        summ = 0
        for bill in self.bills:
            summ += int(bill)
        return summ

    def __int__(self):
        return self.total(bills)


class CashDesk:

    def __init__(self):
        self.money = []

    def take_money(self, currency):
        self.money.append(currency)

    def total(self):
        result = 0
        for money in self.money:
            if isinstance(money, Bill):
                result += int(money)
            elif isinstance(money, BatchBill):
                for i in money:
                    result += int(i)
        return result

    def inspect(self):
        res = {}
        for money in self.money:
            if isinstance(money, Bill):
                if money in res:
                    res[money] += 1
                else:
                    res[money] = 1
            elif isinstance(money, BatchBill):
                for i in money:
                    if i in res:
                        res[i] += 1
                    else:
                        res[i] = 1
        return res


values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]
batch = BatchBill(bills)
desk = CashDesk()
desk.take_money(batch)
desk.take_money(Bill(10))
print(desk.total())
print(desk.inspect())
