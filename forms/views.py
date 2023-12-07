from .models import Enquete, Voto, User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    enquetes = Enquete.objects.all()
    return render(request, "pages/index.html", {'enquetes':enquetes})

def minhas_enquetes(request):
    enquetes = Enquete.objects.filter(Enquete.criador == request.user)
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
    return render(request, "pages/detalhe_enquete.html", {"enquete": enquete})

def finalizar(request, id):
    enquete = Enquete.objects.get(id=id)
    enviar_email_votos(enquete)
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
def opcoes(request, id):
    enquete = get_object_or_404(Enquete, id=id)

    if request.method == 'POST':
        resposta_selecionada = request.POST.get('resposta')

        enquete = Enquete.objects.get(id=id)

        if enquete.opcao1 == resposta_selecionada:
            enquete.opcao1_resultado += 1
        elif enquete.opcao2 == resposta_selecionada:
            enquete.opcao2_resultado += 1
        elif enquete.opcao3 == resposta_selecionada:
            enquete.opcao3_resultado += 1
        elif enquete.opcao4 == resposta_selecionada:
            enquete.opcao4_resultado += 1
        elif enquete.opcao5 == resposta_selecionada:
            enquete.opcao5_resultado += 1
        elif enquete.opcao6 == resposta_selecionada:
            enquete.opcao6_resultado += 1
        
        enquete.save()

        if resposta_selecionada:
            Voto.objects.create(enquete=enquete, resposta=resposta_selecionada, votante=request.user)
            return redirect('home')

    return render(request, "pages/detalhe_enquete.html", {"enquete": enquete})

def resultado(request, id):
    enquete = Enquete.objects.get(id=id)
    return render(request, "pages/resultado_enquete.html")

def enviar_mail(email, enquete):

    msg = MIMEMultipart()
    msg["subject"] = "Enquete Finalizada"
    msg["From"] = credentials.EMAIL
    msg["To"] = email
    corpo_do_email = f"""
    <html>
        <head></head>
        <body>
            <p>Olá, tudo bem?</p>
            <br>
            <p>Passando pra avisar que a enquete "<strong>{enquete.pergunta}</strong>" foi encerrada.</p>
            <p>Acesse a página e confira o final da votação.</p>
            <p>Obrigado!</p>
        </body>
    </html>
    """
    msg.attach(MIMEText(corpo_do_email, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(credentials.EMAIL, credentials.PASSWORD)
        smtp.send_message(msg)

def enviar_email_votos(enquete):
    emails_votantes = []

    for voto in Voto.objects.filter(enquete=enquete):
        emails_votantes.append(voto.votante.email)

    for email in emails_votantes:
        enviar_email(email, enquete)


