from zipfile import ZipFile
import json
from transactions import Transaction
from datetime import datetime

datafile = '..\data\operations.zip'

def show_last_five(datafile):
    trans_list = []
    with ZipFile(datafile) as zip_file:
        with zip_file.open('operations.json') as file:
            data = json.loads(file.read().decode('utf-8'))
            for item in data:
                try:
                    trans_list.append(Transaction(item['id'], datetime.fromisoformat(item['date']), item['state'], item['operationAmount'], item['description'], item.get('from', None), item['to']))
                except:
                    continue

    trans_list.sort(key=lambda x: x.date, reverse=True)

    for i in range(5):
        print(trans_list[i])
        print()


show_last_five(datafile)