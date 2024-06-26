from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm

# Create your views here.


def view_products(request):
    """A view to to see all products, including sorting and searching """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if 'new' in request.GET:
            products = products.filter(new=True)

        if 'on_sale' in request.GET:
            products = products.filter(on_sale=True)

        if 'all_specials' in request.GET:
            products = products.filter(all_specials=True)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to the details of individual product """

    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm(user=request.user, product=product)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.'
                                    'Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.'
                                    'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ Add a review to a product """
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        messages.error(
            request,
            'Sorry, only registered users can do that.'
            'Please login or register to delete a review.'
        )
        return redirect('home')

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.user, product, request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Review successfully added!')
            return redirect('product_detail', product_id=product_id)
        else:
            messages.error(request, 'Failed to add review. Please try again.')
    else:
        form = ReviewForm(request.user, product)
    return render(request, 'products/review.html',
                  {'form': form, 'product': product})


@login_required
def edit_review(request, review_id):
    """ Edit a review """
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        messages.error(
            request,
            'Sorry, only registered users can do that.'
            'Please login or register to delete a review.'
        )
        return redirect('home')

    review = get_object_or_404(Review, pk=review_id)
    product = review.product

    if request.method == 'POST':
        form = ReviewForm(request.user, product, request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review successfully updated!')
            return redirect('product_detail', product_id=product.id)
        else:
            messages.error(request, 'Failed to update review.'
                                    'Please correct the errors.')
    else:
        form = ReviewForm(request.user, product, instance=review)

    return render(request, 'products/edit_review.html', {
                            'form': form,
                            'product': product,
                            'review': review
    })


@login_required
def delete_review(request, review_id):
    """ Delete a review """

    # Check if the user is authenticated
    if not request.user.is_authenticated:
        messages.error(
            request,
            'Sorry, only registered users can do that.'
            'Please login or register to delete a review.'
        )
        return redirect('home')

    # Retrieve the review or return a 404 error if not found
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        # Delete the review
        review.delete()
        messages.success(request, 'Review successfully deleted!')

    return redirect('profile')  # Redirect to the profile page after deletion