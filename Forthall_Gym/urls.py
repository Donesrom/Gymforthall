from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('class', views.classes,name='class'),
    path('contact', views.contact,name='contact'),
]