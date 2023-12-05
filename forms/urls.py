from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home_enquetes/', views.index, name='enquetes'),
]