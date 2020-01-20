from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from cw21.forms import CustomerForm
from cw21.models import Customer


def home(request):
    return render(request, 'home.html')



def add_customer(request):
    if request.method == 'GET':
        context = {'form': CustomerForm()}
        return render(request, 'customer.html', context)
    elif request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Customer.objects.create(
                firstname=data['firstname'],
                lastname=data['lastname'],
                age=data['age'],
                profession=data['profession']
            )
            Customer.objects.create(**data)
            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')
