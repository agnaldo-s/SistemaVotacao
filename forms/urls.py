from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('adicionar-enquete/', views.add_enquete, name='adicionar-enquete')
]