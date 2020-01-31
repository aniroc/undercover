from django.db import models
from product.models import Product

'''
{
   "customer_email": "sally_baker@undercovertourist.com",
   "customer_name": "Sally Baker",
   "customer_phone": "(512) 555-1234",
   "quantity": 2
}

Confirmation Code (confirmation_code)
Product Name
Product Price
Product Cost
Quantity
Customer Name Customer Email Address Customer Phone Number
'''

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=250)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
	confirmation_code = models.CharField(max_length=30)
	order = models.ForeignKey(Order,
    	related_name='items',
    	on_delete=models.CASCADE)
	product = models.ForeignKey(Product,
    	related_name='order_items',
    	on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	cost = models.DecimalField(default=10.00, max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity