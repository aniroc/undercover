from django.urls import path
from . import views
from .views import product_list_json, product_detail_json, update_products
from cart.views import cart_detail

# working:  http://127.0.0.1:8000/excursions/tickets/
# /excursions/tickets/?name=fun_list

app_name = 'product'

urlpatterns = [
	path('cart/', cart_detail, name='cart_detail'),
    path("tickets-api/", product_list_json, name="fun_list"),
    path("ticket_detail-api/<int:pk>/", product_detail_json, name="ticket_detail"),
    path("update_tickets/", update_products, name="update"),
    path('', views.product_list, name='product_list'),
    path('tickets/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/', views.product_detail,
         name='product_detail'),
]