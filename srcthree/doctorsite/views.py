from django.core.mail import send_mail
from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib import messages

from doctorsite.forms import PatientForm, SendEmailForm
from doctorsite.models import Patient

# Create your views here.
from django.http import HttpResponse
def index(request):
   return HttpResponse("Hello world")



def home(request):
    patients = Patient.objects.filter()
    return render(request, 'home.html', {'patients': patients})



def select(request):
    if request.method == 'GET':
        context = {'form': PatientForm()}
        return render(request, 'select.html', context)
    elif request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            patient= Patient.objects.create(**data)


            messages.add_message(
                request,
                messages.INFO,
                f'patient "{patient.firstname} {patient.lastname}" created successfully',
            )
            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')

def add(request):
    if request.method == 'GET':
        context = {'form': PatientForm()}
        return render(request, 'add.html', context)
    elif request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            patient= Patient.objects.create(**data)

            messages.add_message(
                request,
                messages.INFO,
                f'patient "{patient.firstname} {patient.lastname}" created successfully',
            )
            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')

def send_email(request):
    if request.method == 'GET':
        return render(request, 'send_email.html', {'form': SendEmailForm()})
    elif request.method == 'POST':
        data = SendEmailForm(request.POST)
        if data.is_valid():
            cleaned_data = data.cleaned_data
            send_mail(
                cleaned_data.get('topic'),
                cleaned_data.get('message'),
                cleaned_data.get('sender'),
                [cleaned_data.get('receiver')],
                fail_silently=False,
            )
    return redirect(send_email)