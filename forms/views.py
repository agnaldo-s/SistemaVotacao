from .models import Enquete, Voto, User
from django.shortcuts import render, redirect
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
def votar_enquete(request, id):
    enquete = Enquete.objects.get(id=id)

    # Verificar se o usuário já votou na enquete
    # if Voto.objects.filter(enquete=enquete, votante=request.user).exists():
    #     messages.error(request, "Você já votou nesta enquete.")
    #     return redirect('votar-enquete')

    if request.method == 'POST':
        opcao_selecionada = request.POST['opcao']
        if opcao_selecionada == 'opcao1':
            enquete.opcao1 += 1
        elif opcao_selecionada == 'opcao2':
            enquete.opcao2 += 1
        elif opcao_selecionada == 'opcao3':
            enquete.opcao3 += 1
        elif opcao_selecionada == 'opcao4':
            enquete.opcao4 += 1
        elif opcao_selecionada == 'opcao5':
            enquete.opcao5 += 1
        elif opcao_selecionada == 'opcao6':
            enquete.opcao6 += 1

        # Verificar se o usuário escolheu exatamente uma opção
        # if len(opcoes_votadas) != 1:
        #     messages.error(request, "Escolha exatamente uma opção para votar.")
        #     return redirect('home')

        # Registrar o voto no banco de dados
        Voto.objects.create(enquete=enquete, resposta=opcao_selecionada, votante=request.user)
        messages.success(request, "Voto registrado com sucesso!")

        return redirect('votar-enquete')

    # Verificar se o usuário já votou e preencher as opções escolhidas
    voto_do_usuario = Voto.objects.filter(enquete=enquete, votante=request.user).first()
    opcoes_escolhidas = [voto_do_usuario.resposta] if voto_do_usuario else []

    return render(request, "detalhe-enquete", {"enquete": enquete, "opcoes_escolhidas": opcoes_escolhidas})
