from django.contrib import admin
from .models import Customer, MailTemplate, Post

admin.site.register(Customer)
admin.site.register(MailTemplate)
admin.site.register(Post)
