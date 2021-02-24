# Before Start 🐱‍👤
DB에 데이터를 업로드 시키는 방법은 정말 무수히 많습니다. 
3rd party package중 단연코 데이터를 관리하고 정제하는데 우수한 pandas라는 라이브러리도 있지만 이번에는 순수 파이썬과 loop문을 이용하고 그리고 `django orm`을 이용해 db를 조회하고 저장 시켜보도록 할게요. 

# Get the Point😉

## Git clone & Default setup😆

1. 깃 클론하기
`git clone https://github.com/hyeseong-dev/db_uploader.git`

2. 가상환경 생성 및 설치 

```python
# 윈도우 기준
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

3. DB 껍데기 만들기

> 
$ mysql -uroot -p;
$ create database 디비이름;

4. migrations & migrate

>$ python manage.py makemigrations && python manage.py migrate



## Descriptions of source code😎 

### csv 파일

```
menu,category,product,price
음료,콜드 브루 커피,나이트로 바닐라 크림,100
음료,콜드 브루 커피,제주 비자림 콜드,100
음료,콜드 브루 커피,코코넛 화이트 콜드 브루,100
음료,콜드 브루 커피,나이트로 쇼콜라 클라우드,100
음료,콜드 브루 커피,콜드 브루 몰트,100
음료,브루드 커피,아이스 커피,100
음료,브루드 커피,오늘의 커피,100
음료,에스프레소,에스프레소 콘 파나,100
음료,에스프레소,에스프레소 마키아또,100
음료,에스프레소,카페 아메리카노,100
음료,프라푸치노,더블 에스프레소 칩 프라푸치노,100
음료,프라푸치노,블랙 와플칩 크림 프라푸치노,100
음료,프라푸치노,피스타치오 크림 프라푸치노,100
음료,블렌디드,피치 & 레몬 블렌디드,100
음료,블렌디드,망고 패션 후르츠 블렌디드,100
음료,블렌디드,딸기 요거트 블렌디드,100
음료,블렌디드,망고 바나나 블렌디드,100
음료,블렌디드,익스트림 티 블렌디드,100
음료,스타벅스 피지오,매직 팝 스플래쉬 피지오,100
음료,스타벅스 피지오,블랙 티 레모네이드 피지오,100
음료,스타벅스 피지오,쿨 라임 피지오,100
음료,스타벅스 피지오,패션 탱고 티 레모네이드 피지오,100
음료,스타벅스 피지오,핑크 자몽 피지오,100
음료,티(티바나),피치 젤리 핫 티,100
음료,티(티바나),피치 젤리 아이스 티,100
음료,기타 제조 음료,시그니처 핫 초콜릿,100
음료,기타 제조 음료,아이스 시그니처 초콜릿,100
음료,기타 제조 음료,플러피 판다 핫 초콜릿,100
푸드,베이커리,녹차 머핀,100
푸드,베이커리,다크 초콜릿 칩 머핀,100
푸드,베이커리,상큼한 블루베리 머핀,100
푸드,케이크,서머 베리 요거트 케이크,100
푸드,케이크,7 레이어 가나슈 케이크,100
푸드,케이크,레드벨벳 크림치즈 케이크,100
푸드,케이크,마스카포네 티라미수 케이크,100
푸드,샌드위치 & 샐러드,베이컨 포테이토 롤,100
푸드,샌드위치 & 샐러드,스크램블 에그 롤,100
푸드,샌드위치 & 샐러드,애플 까망베르 샌드위치,100
푸드,샌드위치 & 샐러드,트리플 머쉬룸 치즈 샌드위치,100
푸드,따뜻한 푸드,트러플 머쉬룸 수프,100
푸드,따뜻한 푸드,현미 크림 수프,100
푸드,과일 & 요거트,사과 가득 핸디 젤리,100
푸드,과일 & 요거트,제주 자연 청 세트,100
푸드,과일 & 요거트,하루 한 컵 RED,100
푸드,스낵 & 미니 디저트,로고 코인 다크 초콜릿 (골드),100
푸드,스낵 & 미니 디저트,로스티드 아모든 앤 초콜릿,100
푸드,아이스크림,유기농 바닐라 아이스크림,100
푸드,아이스크림,유기농 초콜릿 아이스크림,100
상품,머그,,100
상품,글라스,,100
상품,플라스틱 텀블러,,100
상품,스테인리스 텀블러,,100
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
print('Current dir의 경로 : ', end=''), print(os.getcwd())               # os가 파악한 현재 경로를 표기
print('os.path.abspath(__file__)의 경로 : ',os.path.abspath(__file__))    # 현재 작업중인 파일을 포함 경로를 구체적으로 표기
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('BASE_DIR=', end=''), print(BASE_DIR)
print('똑같나? 다르나?', BASE_DIR == os.getcwd()) # 소문자 c , 대문자 C 차이 때문인것 같네요.

sys.path.append(BASE_DIR)  # sys 모듈은 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈이다. sys에 대해서는 뒤에서 자세하게 다룰 것이다. 이 sys 모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉터리를 확인할 수 있다.

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'westarbucks.settings') 
 # python이 실행될 때 DJANGO_SETTINGS_MODULE라는 환경 변수에
# 현재 프로젝트의 settings.py 파일 경로를 등록
django.setup() # python manage.py shell 을 실행하는 것이랑 비슷한 방법이다. 즉 파이썬 파일에서도 django를 실행 시킬수 있다.

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

## Check Points✨
사실 db 작업을 하다보면 예상치 못한 오류와 버그에 진입하는 것은 숙명에 가깝지 않을까? 생각합니다. 

그래서 DB 명령어에 친숙해져야 하는데요. 
RDBMS의 경우에는 특히 각 DB컬럼간의 제약조건 때문에 더 초보들에게는 진입장벽이 높아요.

그래서 간단히 제약조건을 풀어버리는 명령어를 소개합니다.
```sql
SET FOREIGN_KEY_CHECKS = 0; -- Disable foreign key checking. TRUNCATE TABLE Video; TRUNCATE TABLE Category; SET FOREIGN_KEY_CHECKS = 1; -- Enable foreign key checking.
```
truncate 문으로 테이블 다 비우고 나서 다시 값을 1로 설정해주세요~

참고자료: [코드의추억](https://wookmania.tistory.com/113)
