from django.shortcuts import render
from .models import Customer, MailTemplate

def index(request):
    customers = Customer.objects.all()
    return render(request, 'mail/index.html', {'customers': customers})

def customer(request, id):
    customer = Customer.objects.get(id=id)
    templates = MailTemplate.objects.all()
    return render(request, 'mail/customer.html', {
        'customer': customer,
        'templates': templates,
        })
