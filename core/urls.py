from django.contrib import admin
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('product.urls', namespace='index')),
	path('excursions/', include('product.urls')),
    path('admin/', admin.site.urls)
]
