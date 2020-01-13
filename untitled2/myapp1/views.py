from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def index(request):
    if request.method == 'GET':
        template = loader.get_template('index.html')
        return HttpResponse(template.render(request=request))
    elif request.method == 'POST':
        field = [request.POST.get('firstname'), request.POST.get('lastname'), request.POST.get('age'),
                 request.POST.get('comment')]
        print(field)
        template = loader.get_template('index.html')

        return HttpResponse(template.render(request=request))
