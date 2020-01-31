from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from cart.forms import CartAddProductForm

from .models import Product
import requests


def index(request):
    responseData = {
        'id': 4,
        'name': 'Test Response',
        'roles' : ['Admin','User']
    }

    return JsonResponse(responseData)

def product_list_json(request):
    products = Product.objects.all()
    data = {"results": list(products.values("id", "uuid", "name", "slug", "price", "details"))}

    return JsonResponse(data)


def product_detail_json(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = {"results": {
        "id": product.id, 
        "uuid": product.uuid, 
        "name": product.name, 
        "slug": product.slug, 
        "price": product.price,
        "details": product.details
    }}

    return JsonResponse(data)

def update_products(request):
	response = requests.get(
    	'http://careers.undercovertourist.com/assignment/1/products/',
    	headers={'X-Auth': 'user.name'},
	)
	json_response = response.json()['results']
	products = Product.objects.all()

	for ticket in json_response:
		if products.filter(Q(id=ticket.get('id'))).exists():
			print('Updating Price:  ', ticket.get('id'))
			#select_for_update(nowait=False, skip_locked=False, of=())¶ #TODO
			products.filter(Q(id=ticket.get('id'))).update(price=ticket.get('price'))
		else:
			try:
				print('Creating Ticket:  ', ticket.get('id'))
				products.create(
					id=ticket.get("id"), 
					uuid=ticket.get("uuid"), 
					name=ticket.get("name"), 
					slug=ticket.get("slug"), 
					price=ticket.get("price")
					)
			except Exception as e:
				print("Error creating ticket:  ", ticket)
				return JsonResponse(e)

	responseData = {
        'data': "Update Successful"
    }
	return JsonResponse(responseData)

def product_list(request, category_slug=None):
    products = Product.objects.filter(qoh__gt=0)

    return render(request,
                  'excursions/product/list.html',
                  {'products': products})

def product_detail(request, id):  
    product = get_object_or_404(Product,
                                id=id,
                                ) 
    cart_product_form = CartAddProductForm()
    return render(request,
                  'excursions/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


