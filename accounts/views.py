from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")

        if not all([user, password]):
            messages.error(request, "Favor, preencha todos os campos.")
            return redirect("login")

        user = authenticate(request, username=user, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Usuário ou senha incorretos.")
            return redirect("login")


from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        user = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not all([user, email, password]):
            messages.error(request, "Favor, preencha todos os campos.")
            return redirect("register")

        try:
            if User.objects.filter(email=email).exists():
                messages.error(request, "E-mail já cadastrado.")
                return redirect("register")

            User.objects.create_user(username=user, email=email, password=password)
            messages.success(request, "Conta criada com sucesso.")
            messages.success(request, "Faça o login.")
            return redirect("login")

        except IntegrityError as e:
            if "UNIQUE constraint failed: auth_user.username" in str(e):
                messages.error(request, "Nome de usuário existente.")
            else:
                messages.error(request, "Erro ao criar a conta.")

    return render(request, "pages/register.html")



def logout(request):
    auth.logout(request)
    return redirect("login")
