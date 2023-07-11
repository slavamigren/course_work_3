from zipfile import ZipFile
import json
from transactions import Transaction
from datetime import datetime

datafile = '..\data\operations.zip' # адрес архива с данными

def show_last_five(datafile):
    '''выводит пять последних удачных операций'''
    trans_list = [] # сюда выгружаем данные
    with ZipFile(datafile) as zip_file:
        with zip_file.open('operations.json') as file:
            data = json.loads(file.read().decode('utf-8'))
            for item in data: # переносим всё в список экземпляров класса Transaction, если данных не достаточно, просто пропускаем запись (это не касается открытия вклада, где есть только счет получатель)
                try:
                    trans_list.append(Transaction(item['id'], datetime.fromisoformat(item['date']), item['state'], item['operationAmount'], item['description'], item.get('from', None), item['to']))
                except:
                    continue

    trans_list.sort(key=lambda x: x.date, reverse=True) # сортируем по дате и времени

    final_list = filter(lambda x: x.state == 'EXECUTED', trans_list) # итератор на только состоявшиеся транзакции

    for i in range(5):# выводим пять последних операций
        print(next(final_list))
        print()


show_last_five(datafile)