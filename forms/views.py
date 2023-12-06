from .models import Enquete, Voto, User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    enquetes = Enquete.objects.all()
    return render(request, "pages/index.html", {'enquetes':enquetes})

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

        if (
            not pergunta
            or not opcao1
            or not opcao2
            or not opcao3
            or not opcao4
            or not opcao5
            or not opcao6
        ):
            messages.error(request, "Por favor, preencha todos os campos.")
            return redirect("add-enquete")
        
        if not pergunta.split():
            messages.error(request, "A pergunta deve começar com letra.")
            return redirect("add-enquete")
        
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
    
def detalhe(request, id):
    enquete = Enquete.objects.get(id=id)
    if enquete.criador == request.user:
        
    return render(request, "pages/detalhe_enquete.html", {"enquete": enquete})

def finalizar(request, id):
    enquete = Enquete.objects.get(id=id)
    enquete.delete()
    return redirect ('home')

def buscar_enquete(request):
    q = request.GET.get("q")
    enquetes = Enquete.objects.all()
    if q:
        enquetes = enquetes.filter(pergunta__icontains=q)
    for enquete in enquetes:
        enquete.status = 'Aberta' if enquete.finalizado else 'Fechada'
    return render(request, "pages/index.html", {"enquetes": enquetes})


@login_required
def votar(request, id):
    enquete = get_object_or_404(Enquete, id=id)

    if request.method == 'POST':
        resposta_selecionada = request.POST.get('resposta')
        if resposta_selecionada:
            Voto.objects.create(enquete=enquete, resposta=resposta_selecionada, votante=request.user)
            return redirect('detalhe_enquete', id=enquete.id)

    return render(request, "pages/detalhe_enquete.html", {"enquete": enquete})

def resultado(request, id):
    enquete = Enquete.objects.get(id=id)
    return render(request, "pages/resultado_enquete.html")


