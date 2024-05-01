from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    different_size = models.BooleanField(default=False)
    description = models.TextField()
    new = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)
    all_specials = models.BooleanField(default=False)
    details = models.CharField(max_length=360)
    materials = models.CharField(max_length=254, null=True, default=None)
    fabric_care = models.CharField(max_length=360)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image = models.ImageField(null=True, blank=True)
    size = models.CharField(max_length=254, null=True, blank=True)
    weight = models.CharField(max_length=254, null=True, blank=True)
    special_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, default=0)

    def update_rating(self):
        # Calculate the average rating for the product's reviews
        avg_rating = self.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
        if avg_rating is not None:
            # Update the product's rating field with
            # the calculated average rating
            self.rating = round(avg_rating, 2)
            self.save()

    def _str_(self):
        return self.name


class Review(models.Model):
    """ The review model for the products app """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews'
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
    )
    # Validator info found here:
    # https://docs.djangoproject.com/en/3.2/ref/validators/#minvaluevalidator
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.update_rating()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.product.update_rating()

    def __str__(self):
        return f"{self.user.username}'s Review for {self.product.name}"

