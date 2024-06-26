from django.db import models
from django.utils import timezone

class Contact(models.Model):
    """Model to represent a contact form submission."""

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    date_submitted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Forms"
        ordering = ["-date_submitted"]
