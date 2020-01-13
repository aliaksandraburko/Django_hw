from django.urls import path

from myapp1.views import index

urlpatterns = [
    path('index', index, name='index')
]