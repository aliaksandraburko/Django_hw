from django.urls import path
from cw21.views import home,add_customer

urlpatterns=[
    path('home', home, name='home'),
    path('add', add_customer, name='add_customer'),

]