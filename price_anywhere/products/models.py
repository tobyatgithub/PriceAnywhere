from django.db import models

# Everything here shall be nullable
class Product(models.Model):
    upc = models.CharField(max_length=50, null=True, blank=True) # unique product code
    title = models.CharField(max_length=255, null=True, blank=True)
    manufactor = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title