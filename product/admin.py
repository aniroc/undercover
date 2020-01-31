from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'uuid', 'name', 'slug', 'price',
                    'qoh', 'details']
    list_filter = ['id', 'name', 'qoh']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}