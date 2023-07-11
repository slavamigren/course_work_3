from datetime import datetime


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
        '''преобразует в строку нужного формата'''
        if self.from_w:
            return f'''{self.date.strftime('%d.%m.%Y')} {self.description}
{self.proceed_from_str(self.from_w)} -> {self.proceed_from_str(self.to_w)}
{self.operationAmount['amount']} {self.operationAmount['currency']['name']}'''
        else:
            return f'''{self.date.strftime('%d.%m.%Y')} {self.description}
{self.proceed_from_str(self.to_w)}
{self.operationAmount['amount']} {self.operationAmount['currency']['name']}'''


    @staticmethod
    def proceed_from_str(string):
        '''заменяет часть цифр в строке со счетом на звёздочки'''
        if string.split()[0] == 'Счет':
            return f'Счет **{string.split()[-1][-4:]}'
        else:
            return f'{" ".join(string.split()[:-1])} {string.split()[-1][:4]} {string.split()[-1][5:7]}** **** {string.split()[-1][-4:]}'


