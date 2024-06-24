from django.db import models
from ckeditor.fields import RichTextField

CATEGORIES = (
    ('prospect', 'prospect'),
    ('lead', 'lead'),
    ('customer', 'customer'),
)

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORIES, default="prospect")

    def __str__(self):
        return(f"{self.name}")
    
class MailTemplate(models.Model):
    text = models.TextField(max_length=2000)
    tag = models.CharField(max_length=50, choices=CATEGORIES, default="prospect")

    def __str__(self):
        return(f"{self.tag}")
    
class Post(models.Model):
    content = RichTextField()