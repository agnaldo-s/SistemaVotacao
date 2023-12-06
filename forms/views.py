from .models import Enquete, Voto, User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "pages/index.html")


def busca_enquete(request):
    q = request.GET.get("q")
    enquetes = Enquete.objects.filter(pergunta__icontains=q)
    if len(enquetes) > 0:
        return render(request, "pages/index.html", {"enquetes": enquetes})
    else:
        return render(request, "pages/index.html", {"erro": "Não foi encontrado nada"})


def add_enquete(request):

    if request.method == 'POST':
        pergunta = request.POST.get('pergunta')
        opcao1 = request.POST.get('opcao1')
        opcao2 = request.POST.get('opcao2')
        opcao3 = request.POST.get('opcao3')
        opcao4 = request.POST.get('opcao4')
        opcao5 = request.POST.get('opcao5')
        opcao6 = request.POST.get('opcao6')
        criador = request.user
        
  
        Enquete.objects.create(
            pergunta = pergunta,
            opcao1 = opcao1,
            opcao2 = opcao2,
            opcao3 = opcao3,
            opcao4 = opcao4,
            opcao5 = opcao5,
            opcao6 = opcao6,
            criador = criador
        )

        return redirect('home')

    else:
        return render(request, "pages/adicionar_enquete.html")
    
    
