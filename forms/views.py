from .models import Enquete, Voto
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='index')
def index(request):
    return render(request, "pages/login.html")

@login_required(redirect_field_name='login')
def home_enquetes(request):
    enquetes = Enquete.objects.all().order_by("cod")

    for enquete in enquetes:
        print(f"enquete.name + enquete.gender")
    return render(request, "pages/home_enquetes.html", {"enquete": enquetes})