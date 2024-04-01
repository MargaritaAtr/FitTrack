from django.shortcuts import render
from .models import Product

# Create your views here.

def view_products(request):
    """A view to rto see all products, including sorting and searching """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)