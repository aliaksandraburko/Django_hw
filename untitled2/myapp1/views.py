from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


# Create your views here.
from myapp1.forms import UserForm

def user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            age = data.get('age')
            comment = data.get('comment')
            result = f'{firstname}|{lastname}|{age}|{comment}'
            print(result)
        else:
            errors_dict = form.errors
            template = loader.get_template('index.html')
            return HttpResponse(template.render({'errors': errors_dict}, request))
    form = UserForm()
    context = {'form': form}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
    form = UserForm()
    context = {'form': form}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


