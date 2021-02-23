import json
from django.http     import JsonResponse

from django.views    import View
from products.models import Menu, Category, Product


class ProductsView(View):
        def post(self, request):

                data = json.loads(request.body) 
                print('@'*30,data['product'],type(data['product']), type(data),data.get('product').get('price'))
                print('h2222222222')    
                menu     = Menu.objects.create(name=data['menu'])

                category = Category.objects.create(
                        name=data['category'],
                        menu=menu
                )

                product = Product.objects.create(
                        name=data['product']['name'],
                        price=int(data['product']['price']),
                        category=category,
                )
                print('$'*30)

                return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

        def get(self, request):
                products = Product.objects.all()
                results = []
                for product in products:
                        results.append( {
                        "menu":product.category.menu.name,
                        "category":product.category.name,
                        "product" :product.name
                        } )
                return JsonResponse({'resutls':resluts}, status=200)