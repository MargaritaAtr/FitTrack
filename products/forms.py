from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'category',
            'sku',
            'name',
            'description',
            'new',
            'on_sale',
            'details',
            'fabric_care',
            'price',
            'rating',
            'image',
            'size',
            'special_price',
        ]
    image = forms.ImageField(
            label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """
    Form for the product review page.
    """

    class Meta:
        model = Review
        fields = ('rating', 'comment')
        labels = {
            'comment': 'Please provide a brief comment about your experience \
                (max 300 characters)',
        }

    # Define choices for the rating field
    RATING_CHOICES = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        label='Please select a rating between 1 and 5',
        widget=forms.Select(attrs={'class': 'form-select',
                                   'style': 'width: 80px;'})
    )

    def __init__(self, user, product, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'mb-6'
            if field == 'comment':
                self.fields[field].widget.attrs['maxlength'] = '300'
                self.fields[field].widget.attrs['minlength'] = '5'


