from _operator import index

from django.urls import path

from myapp1.views import *

urlpatterns = [
    path('index', index, name='index'),
    # path('user', user_view, name='user'),
]
