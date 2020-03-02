from django.urls import path

from doctorsite.views import index, home, select, add, send_email

urlpatterns = [
    path(r'index/', index, name='index'),
    path(r'home/', home, name='home'),
    path(r'', add, name='add'),
    path(r'select/', select, name='select'),
    path('send_email/', send_email, name='send_email'),
]

