class Transaction:
    def __init__(self, id, date, state, operationAmount, description, from_w, to_w):
        self.id = id
        self.date = date
        self.state = state
        self.operationAmount = operationAmount
        self.description = description
        self.from_w = from_w
        self.to_w = to_w


    def __str__(self):
        return f'''14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.'''


    @staticmethod
    def proceed_from_str(string):
        if string.split()[0] == 'Счет':
            return f'Счет **{string.split()[-1][-4:]}'
        else:
            return f'{" ".join(string.split()[:-1])} {string.split()[-1][:4]} {string.split()[-1][5:7]}** **** {string.split()[-1][-4:]}'






class Transactions:
    def __init__(self):
        self.transact_list = []


    def add_transaction(self, transaction):
        if not isinstance(transaction, Transaction):
            raise ValueError("new adding transaction must be a Transaction type")
        self.transact_list.append(transaction)


    def sort(self) :
        self.transact_list.sort(key=lambda x: x.date, reverse=True)


