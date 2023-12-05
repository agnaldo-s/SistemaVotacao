from .models import Enquete, Voto
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "pages/index.html")


def busca_enquete(request):
    q = request.GET.get("q")
    enquetes = Enquete.objects.all()
    if q:
        enquetes = enquetes.filter(name__icontains=q)
    print(enquetes)
    return render(request, "pages/index.html", {"enquetes": enquetes})

def add_enquete(request):
    return render(request, "pages/adicionar_enquete.html")

