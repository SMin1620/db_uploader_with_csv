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

# Menu Table

def insert_menu():    
    with open(CSV_PATH, newline='', encoding='utf8') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            if not Menu.objects.filter(name=row['menu']).exists():
                menu_id = Menu.objects.create(
                    name = row['menu'] )
    print('MENU DATA UPLOADED SUCCESSFULY!')    

def insert_category():    
    with open(CSV_PATH, newline='', encoding='utf8') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            if not Category.objects.filter(name=row['category']).exists():
                menu_id = Menu.objects.get(name=row['menu'])
                Category.objects.create(
                    name = row['category'], 
                    menu = menu_id, 
                    )
    print('CATEGORY DATA UPLOADED SUCCESSFULY!')    

def insert_products():    
    with open(CSV_PATH, newline='', encoding='utf8') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            # menu_id     = Menu.objects.get(name=row['name'])
            category_id = Category.objects.get(name=row['category'])
            products = row['product'].split(',')
            
            print(products)
            for product in products:
                        
                if not Product.objects.filter(
                                            name=row['product'],
                                            category=category_id).exists():
                                            
                    Product.objects.create(name=row['product'] if row['product'] else category_id.name,
                                           price=row['price'],
                                           category = category_id,)
        print('PRODUCT DATA UPLOADED SUCCESSFULY!')    


insert_menu()
insert_category()
insert_products()