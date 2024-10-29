from newspaper.views import index
from django.urls import path


app_name = 'newspaper'

urlpatterns = [
    path('', index, name='index'),
]