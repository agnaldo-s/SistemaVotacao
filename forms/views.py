from .models import Enquete, Voto
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "pages/index.html")

def add_enquete(request):
    return render(request, "pages/adicionar_enquete.html")