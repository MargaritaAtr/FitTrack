from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name...",
                "class": "rounded-lg w-100"
            }
        ),
    )
    email = forms.EmailField(
        max_length=150,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email...",
                "class": " rounded-lg w-100"
            }
        ),
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Subject...",
                "class": " rounded-lg w-100"
            }
        ),
    )
    content = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Leave us a message...",
                "class": " rounded-lg message-textarea w-100"
            }
        ),
    )

    class Meta:
        model = Contact
        exclude = ("date_submitted",)
