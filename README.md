# Before Start ๐ฑโ๐ค
DB์ ๋ฐ์ดํฐ๋ฅผ ์๋ก๋ ์ํค๋ ๋ฐฉ๋ฒ์ ์ ๋ง ๋ฌด์ํ ๋ง์ต๋๋ค. 
3rd party package์ค ๋จ์ฐ์ฝ ๋ฐ์ดํฐ๋ฅผ ๊ด๋ฆฌํ๊ณ  ์ ์ ํ๋๋ฐ ์ฐ์ํ pandas๋ผ๋ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ ์์ง๋ง ์ด๋ฒ์๋ ์์ ํ์ด์ฌ๊ณผ loop๋ฌธ์ ์ด์ฉํ๊ณ  ๊ทธ๋ฆฌ๊ณ  `django orm`์ ์ด์ฉํด db๋ฅผ ์กฐํํ๊ณ  ์ ์ฅ ์์ผ๋ณด๋๋ก ํ ๊ฒ์. 

# Get the Point๐

## Git clone & Default setup๐

1. ๊น ํด๋ก ํ๊ธฐ
`git clone https://github.com/hyeseong-dev/db_uploader.git`

2. ๊ฐ์ํ๊ฒฝ ์์ฑ ๋ฐ ์ค์น 

```python
# ์๋์ฐ ๊ธฐ์ค
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

3. DB ๊ป๋ฐ๊ธฐ ๋ง๋ค๊ธฐ

> $ mysql -uroot -p;
$ create database ๋๋น์ด๋ฆ;

4. migrations & migrate

>$ python manage.py makemigrations && python manage.py migrate



## Descriptions of source code๐ 

### csv ํ์ผ

```
menu,category,product,price
์๋ฃ,์ฝ๋ ๋ธ๋ฃจ ์ปคํผ,๋์ดํธ๋ก ๋ฐ๋๋ผ ํฌ๋ฆผ,100
์๋ฃ,์ฝ๋ ๋ธ๋ฃจ ์ปคํผ,์ ์ฃผ ๋น์๋ฆผ ์ฝ๋,100
์๋ฃ,์ฝ๋ ๋ธ๋ฃจ ์ปคํผ,์ฝ์ฝ๋ ํ์ดํธ ์ฝ๋ ๋ธ๋ฃจ,100
์๋ฃ,์ฝ๋ ๋ธ๋ฃจ ์ปคํผ,๋์ดํธ๋ก ์ผ์ฝ๋ผ ํด๋ผ์ฐ๋,100
์๋ฃ,์ฝ๋ ๋ธ๋ฃจ ์ปคํผ,์ฝ๋ ๋ธ๋ฃจ ๋ชฐํธ,100
์๋ฃ,๋ธ๋ฃจ๋ ์ปคํผ,์์ด์ค ์ปคํผ,100
์๋ฃ,๋ธ๋ฃจ๋ ์ปคํผ,์ค๋์ ์ปคํผ,100
์๋ฃ,์์คํ๋ ์,์์คํ๋ ์ ์ฝ ํ๋,100
์๋ฃ,์์คํ๋ ์,์์คํ๋ ์ ๋งํค์๋,100
์๋ฃ,์์คํ๋ ์,์นดํ ์๋ฉ๋ฆฌ์นด๋ธ,100
์๋ฃ,ํ๋ผํธ์น๋ธ,๋๋ธ ์์คํ๋ ์ ์นฉ ํ๋ผํธ์น๋ธ,100
์๋ฃ,ํ๋ผํธ์น๋ธ,๋ธ๋ ์ํ์นฉ ํฌ๋ฆผ ํ๋ผํธ์น๋ธ,100
์๋ฃ,ํ๋ผํธ์น๋ธ,ํผ์คํ์น์ค ํฌ๋ฆผ ํ๋ผํธ์น๋ธ,100
์๋ฃ,๋ธ๋ ๋๋,ํผ์น & ๋ ๋ชฌ ๋ธ๋ ๋๋,100
์๋ฃ,๋ธ๋ ๋๋,๋ง๊ณ  ํจ์ ํ๋ฅด์ธ  ๋ธ๋ ๋๋,100
์๋ฃ,๋ธ๋ ๋๋,๋ธ๊ธฐ ์๊ฑฐํธ ๋ธ๋ ๋๋,100
์๋ฃ,๋ธ๋ ๋๋,๋ง๊ณ  ๋ฐ๋๋ ๋ธ๋ ๋๋,100
์๋ฃ,๋ธ๋ ๋๋,์ต์คํธ๋ฆผ ํฐ ๋ธ๋ ๋๋,100
์๋ฃ,์คํ๋ฒ์ค ํผ์ง์ค,๋งค์ง ํ ์คํ๋์ฌ ํผ์ง์ค,100
์๋ฃ,์คํ๋ฒ์ค ํผ์ง์ค,๋ธ๋ ํฐ ๋ ๋ชจ๋ค์ด๋ ํผ์ง์ค,100
์๋ฃ,์คํ๋ฒ์ค ํผ์ง์ค,์ฟจ ๋ผ์ ํผ์ง์ค,100
์๋ฃ,์คํ๋ฒ์ค ํผ์ง์ค,ํจ์ ํฑ๊ณ  ํฐ ๋ ๋ชจ๋ค์ด๋ ํผ์ง์ค,100
์๋ฃ,์คํ๋ฒ์ค ํผ์ง์ค,ํํฌ ์๋ชฝ ํผ์ง์ค,100
์๋ฃ,ํฐ(ํฐ๋ฐ๋),ํผ์น ์ ค๋ฆฌ ํซ ํฐ,100
์๋ฃ,ํฐ(ํฐ๋ฐ๋),ํผ์น ์ ค๋ฆฌ ์์ด์ค ํฐ,100
์๋ฃ,๊ธฐํ ์ ์กฐ ์๋ฃ,์๊ทธ๋์ฒ ํซ ์ด์ฝ๋ฆฟ,100
์๋ฃ,๊ธฐํ ์ ์กฐ ์๋ฃ,์์ด์ค ์๊ทธ๋์ฒ ์ด์ฝ๋ฆฟ,100
์๋ฃ,๊ธฐํ ์ ์กฐ ์๋ฃ,ํ๋ฌํผ ํ๋ค ํซ ์ด์ฝ๋ฆฟ,100
ํธ๋,๋ฒ ์ด์ปค๋ฆฌ,๋น์ฐจ ๋จธํ,100
ํธ๋,๋ฒ ์ด์ปค๋ฆฌ,๋คํฌ ์ด์ฝ๋ฆฟ ์นฉ ๋จธํ,100
ํธ๋,๋ฒ ์ด์ปค๋ฆฌ,์ํผํ ๋ธ๋ฃจ๋ฒ ๋ฆฌ ๋จธํ,100
ํธ๋,์ผ์ดํฌ,์๋จธ ๋ฒ ๋ฆฌ ์๊ฑฐํธ ์ผ์ดํฌ,100
ํธ๋,์ผ์ดํฌ,7 ๋ ์ด์ด ๊ฐ๋์ ์ผ์ดํฌ,100
ํธ๋,์ผ์ดํฌ,๋ ๋๋ฒจ๋ฒณ ํฌ๋ฆผ์น์ฆ ์ผ์ดํฌ,100
ํธ๋,์ผ์ดํฌ,๋ง์ค์นดํฌ๋ค ํฐ๋ผ๋ฏธ์ ์ผ์ดํฌ,100
ํธ๋,์๋์์น & ์๋ฌ๋,๋ฒ ์ด์ปจ ํฌํ์ดํ  ๋กค,100
ํธ๋,์๋์์น & ์๋ฌ๋,์คํฌ๋จ๋ธ ์๊ทธ ๋กค,100
ํธ๋,์๋์์น & ์๋ฌ๋,์ ํ ๊น๋ง๋ฒ ๋ฅด ์๋์์น,100
ํธ๋,์๋์์น & ์๋ฌ๋,ํธ๋ฆฌํ ๋จธ์ฌ๋ฃธ ์น์ฆ ์๋์์น,100
ํธ๋,๋ฐ๋ปํ ํธ๋,ํธ๋ฌํ ๋จธ์ฌ๋ฃธ ์ํ,100
ํธ๋,๋ฐ๋ปํ ํธ๋,ํ๋ฏธ ํฌ๋ฆผ ์ํ,100
ํธ๋,๊ณผ์ผ & ์๊ฑฐํธ,์ฌ๊ณผ ๊ฐ๋ ํธ๋ ์ ค๋ฆฌ,100
ํธ๋,๊ณผ์ผ & ์๊ฑฐํธ,์ ์ฃผ ์์ฐ ์ฒญ ์ธํธ,100
ํธ๋,๊ณผ์ผ & ์๊ฑฐํธ,ํ๋ฃจ ํ ์ปต RED,100
ํธ๋,์ค๋ต & ๋ฏธ๋ ๋์ ํธ,๋ก๊ณ  ์ฝ์ธ ๋คํฌ ์ด์ฝ๋ฆฟ (๊ณจ๋),100
ํธ๋,์ค๋ต & ๋ฏธ๋ ๋์ ํธ,๋ก์คํฐ๋ ์๋ชจ๋  ์ค ์ด์ฝ๋ฆฟ,100
ํธ๋,์์ด์คํฌ๋ฆผ,์ ๊ธฐ๋ ๋ฐ๋๋ผ ์์ด์คํฌ๋ฆผ,100
ํธ๋,์์ด์คํฌ๋ฆผ,์ ๊ธฐ๋ ์ด์ฝ๋ฆฟ ์์ด์คํฌ๋ฆผ,100
์ํ,๋จธ๊ทธ,,100
์ํ,๊ธ๋ผ์ค,,100
์ํ,ํ๋ผ์คํฑ ํ๋ธ๋ฌ,,100
์ํ,์คํ์ธ๋ฆฌ์ค ํ๋ธ๋ฌ,,100
```

### models.py
```python
from django.db import models


class Menu(models.Model):
		name = models.CharField(max_length=20)


class Category(models.Model):
		name = models.CharField(max_length=20)
		menu = models.ForeignKey('Menu', on_delete=models.CASCADE)


class Product(models.Model):
		name  = models.CharField(max_length=100)
		price = models.IntegerField()
		category = models.ForeignKey('Category', on_delete=models.CASCADE)
```

### db_uploaders.py

```python
import os
import django
import csv
import sys


# system setup
os.chdir('.')
print('Current dir์ ๊ฒฝ๋ก : ', end=''), print(os.getcwd())               # os๊ฐ ํ์ํ ํ์ฌ ๊ฒฝ๋ก๋ฅผ ํ๊ธฐ
print('os.path.abspath(__file__)์ ๊ฒฝ๋ก : ',os.path.abspath(__file__))    # ํ์ฌ ์์์ค์ธ ํ์ผ์ ํฌํจ ๊ฒฝ๋ก๋ฅผ ๊ตฌ์ฒด์ ์ผ๋ก ํ๊ธฐ
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('BASE_DIR=', end=''), print(BASE_DIR)
print('๋๊ฐ๋? ๋ค๋ฅด๋?', BASE_DIR == os.getcwd()) # ์๋ฌธ์ c , ๋๋ฌธ์ C ์ฐจ์ด ๋๋ฌธ์ธ๊ฒ ๊ฐ๋ค์.

sys.path.append(BASE_DIR)  # sys ๋ชจ๋์ ํ์ด์ฌ์ ์ค์นํ  ๋ ํจ๊ป ์ค์น๋๋ ๋ผ์ด๋ธ๋ฌ๋ฆฌ ๋ชจ๋์ด๋ค. sys์ ๋ํด์๋ ๋ค์์ ์์ธํ๊ฒ ๋ค๋ฃฐ ๊ฒ์ด๋ค. ์ด sys ๋ชจ๋์ ์ฌ์ฉํ๋ฉด ํ์ด์ฌ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๊ฐ ์ค์น๋์ด ์๋ ๋๋ ํฐ๋ฆฌ๋ฅผ ํ์ธํ  ์ ์๋ค.

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'westarbucks.settings') 
 # python์ด ์คํ๋  ๋ DJANGO_SETTINGS_MODULE๋ผ๋ ํ๊ฒฝ ๋ณ์์
# ํ์ฌ ํ๋ก์ ํธ์ settings.py ํ์ผ ๊ฒฝ๋ก๋ฅผ ๋ฑ๋ก
django.setup() # python manage.py shell ์ ์คํํ๋ ๊ฒ์ด๋ ๋น์ทํ ๋ฐฉ๋ฒ์ด๋ค. ์ฆ ํ์ด์ฌ ํ์ผ์์๋ django๋ฅผ ์คํ ์ํฌ์ ์๋ค.

# import model
from products.models import *

# insert data while reading csv file into table
CSV_PATH = './csv/wecode.csv'

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
            category_id = Category.objects.get(name=row['category'])
            products = row['product'].split(',')
                        
            if not Product.objects.filter(name=row['product'],
                                        category=category_id).exists():                                       
                Product.objects.create(name=row['product'] if row['product'] else category_id.name,
                                    price=row['price'],
                                    category = category_id,)
        print('PRODUCT DATA UPLOADED SUCCESSFULY!')    


insert_menu()
insert_category()
insert_products()
```

## Check Pointsโจ
์ฌ์ค db ์์์ ํ๋ค๋ณด๋ฉด ์์์น ๋ชปํ ์ค๋ฅ์ ๋ฒ๊ทธ์ ์ง์ํ๋ ๊ฒ์ ์๋ช์ ๊ฐ๊น์ง ์์๊น? ์๊ฐํฉ๋๋ค. 

๊ทธ๋์ DB ๋ช๋ น์ด์ ์น์ํด์ ธ์ผ ํ๋๋ฐ์. 
RDBMS์ ๊ฒฝ์ฐ์๋ ํนํ ๊ฐ DB์ปฌ๋ผ๊ฐ์ ์ ์ฝ์กฐ๊ฑด ๋๋ฌธ์ ๋ ์ด๋ณด๋ค์๊ฒ๋ ์ง์์ฅ๋ฒฝ์ด ๋์์.

๊ทธ๋์ ๊ฐ๋จํ ์ ์ฝ์กฐ๊ฑด์ ํ์ด๋ฒ๋ฆฌ๋ ๋ช๋ น์ด๋ฅผ ์๊ฐํฉ๋๋ค.
```sql
SET FOREIGN_KEY_CHECKS = 0; -- Disable foreign key checking. TRUNCATE TABLE Video; TRUNCATE TABLE Category; SET FOREIGN_KEY_CHECKS = 1; -- Enable foreign key checking.
```
truncate ๋ฌธ์ผ๋ก ํ์ด๋ธ ๋ค ๋น์ฐ๊ณ  ๋์ ๋ค์ ๊ฐ์ 1๋ก ์ค์ ํด์ฃผ์ธ์~

์ฐธ๊ณ ์๋ฃ: [์ฝ๋์์ถ์ต](https://wookmania.tistory.com/113)
