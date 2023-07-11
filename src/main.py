from zipfile import ZipFile
import json

with ZipFile('..\data\operations.zip') as zip_file:
    with zip_file.open('operations.json') as file:
        data = json.loads(file.read().decode('utf-8'))
        for i in data:
            if i['description'].split()[0] == 'Перевод':
                print(i['from'])