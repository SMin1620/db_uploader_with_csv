import os
import django
import csv
import sys


# system setup
os.chdir('.')
print('Current dir=', end=''), print(os.getcwd())
print('os.path.abspath(__file__)',os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('BASE_DIR=', end=''), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'westarbucks.settings')
django.setup()

# import model
from products.models import *

# insert data while reading csv file into table
CSV_PATH = '../csv/wecode.csv'

# open csv file and insert row data in MySQL
with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    menu_name = set()
    category_name = set()
    for row in data_reader:
        menu_name.add(row['menu'])
        category_name.add(row['category'])
    for row in data_reader:
        print('hola~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(menu_name)
        if not row['menu'] in menu_name :
            menu_id = Menu.objects.create(
                name = row['menu']
                )
            print(menu_id, 'created!!!!')
            print(menu_id.name)
            # category_id = Category.objects.create(
            #     name=row['category'],
            #     menu=menu_id,
            # )
            # Product.objects.create(
            #     name=row['product'],
            #     price=row['price'],
            #     category=category_id,
            # )
print('DATAS UPLOADED SUCCESSFULY!')
