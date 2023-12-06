from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('add-enquete/', views.add_enquete, name='add-enquete'),
    path('detalhe-enquete/<int:id>/', views.detalhe, name='detalhe-enquete'),
    path('finalizar-enquete/<int:id>/', views.finalizar, name='finalizar-enquete'),
    path("buscar_enquete/", views.buscar_enquete, name="buscar-enquete"),
    path("detalhe-enquete/<int:id>/", views.votar, name="votar-enquete"),
    path('resultado-enquete/<int:id>/', views.resultado, name='resultado-enquete'),
    path('voto/<int:id>/', views.votar, name='voto')
]