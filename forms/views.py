from .models import Enquete, Voto
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def index(request):
    enquetes = Enquete.objects.all().order_by("cod")

    for enquete in enquetes:
        print(f"enquete.name + enquete.gender")
    return render(request, "pages/index.html", {"enquete": enquetes})
