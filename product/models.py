import uuid
from django.db import models
from django.urls import reverse
# Excursion ticket models


class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    #date_created = models.DateTimeField(auto_now_add=True)
    #date_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    #image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    #short_description = models.TextField(blank=True)
    #short_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField(default="Admission to one or more of the following Resort attractions for each day of the ticket")
    qoh = models.IntegerField(default=10)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_detail',
            args=[self.id])  #. , self.slug
