from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        if not usuario or not senha:
            messages.error(request, "Preencha todos os dados.")
            return (request, 'pedidos/login.html')

        
        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Sua conta está desativada.")
        else:
            messages.error(request, "Credenciais inválidas. Tente novamente.")

    return render(request, 'pedidos/login.html')

    

def home(request):
    pass


def logout_view(request):
    logout(request)
    return redirect('login')
