from django.contrib import admin
from .models import Product, Category , Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ReviewAdmin(admin.ModelAdmin):
    """ Review admin - to adjust how it is displayed in the admin panel"""

    list_display = (
        'product',
        'user',
        'rating',
        'created_date',
        'comment',
    )

    ordering = ('product',)    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)