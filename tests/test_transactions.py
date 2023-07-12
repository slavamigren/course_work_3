from src import transactions
from datetime import datetime
import pytest

d = {'id': 957763565, 'state': 'EXECUTED', 'date': '2019-01-05T00:52:30.108534', 'operationAmount': {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 46363668439560358409', 'to': 'Счет 18889008294666828266'}


def  test_proceed_from_str():
    assert transactions.Transaction.proceed_from_str('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'
    assert transactions.Transaction.proceed_from_str('Счет 10848359769870775355') == 'Счет **5355'

def test_str():
    assert str(transactions.Transaction(d['id'], datetime.fromisoformat(d['date']), d['state'], d['operationAmount'], d['description'], d.get('from', None), d['to'])) == '05.01.2019 Перевод со счета на счет\nСчет **8409 -> Счет **8266\n87941.37 руб.'
