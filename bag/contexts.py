from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def apply_discount(original_price, discount_code):
    """
    Apply discount based on the provided discount code.

    Args:
        original_price (float): The original price of the purchase.
        discount_code (str): The discount code entered by the user.

    Returns:
        float: The discounted price after applying the discount code.
    """
    # Define discount codes and their corresponding discount percentages
    discount_codes = {
        "SAVE10": 10,  # 10% discount
        "SAVE20": 20,  # 20% discount
       
    }

    # Check if the discount code is valid
    if discount_code in discount_codes:
        discount_percentage = discount_codes[discount_code]
        discount_amount = (discount_percentage / 100) * original_price
        discounted_price = original_price - discount_amount
        return discounted_price
    else:
        # If the discount code is invalid, return the original price
        return original_price

def bag_contents(request):
    # Initialize variables
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    original_price = 0
    discount_code = request.GET.get('discount_code')  # Assuming discount_code is passed as a query parameter

    # Calculate total and product count based on bag items
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Calculate delivery cost and free delivery threshold
    if product_count > 0 and total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY_COST)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Apply discount code if provided
    if discount_code:
        original_price = total
        total = apply_discount(original_price, discount_code)

    # Calculate grand total
    grand_total = delivery + total

    # Prepare context data
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context