from django.db import models
from products.models import Product
## TODO: 2023-12-17:
## I think its good idea from gpt to add the following models:
## User, Category, Store.


# Purchase record, each row is one product bought.
class PurchaseRecord(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_unit = models.CharField(max_length=255, null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    weight_unit = models.CharField(max_length=255, null=True, blank=True)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateField()
    store = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    product_photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)
    has_discount = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.product_name}"  # Adjust the representation as needed
