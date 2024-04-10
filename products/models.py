from django.db import models

# Create your models here.
class Category (models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def _str_(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    different_size = models.BooleanField(default=False)
    description = models.TextField() 
    new = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)
    all_specials = models.BooleanField(default=False)
    details = models.CharField(max_length=360)
    materials = models.CharField(max_length=254, null=True,default=None)
    fabric_care = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    size = models.CharField(max_length=254, null=True, blank=True)
    weight =  models.CharField(max_length=254, null=True, blank=True)
    special_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, default=0)

    def _str_(self):
        return self.name


class ProductSize_stock(models.Model):

    
    # product = models.ForeignKey(
    #     Product, null=False, blank=False, on_delete=models.CASCADE,
    #     related_name='variants'
    # )
    size = models.IntegerField(default=0, null=False, blank=False)
    stock_count = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.product.name} - {self.size}"
