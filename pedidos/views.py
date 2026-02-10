from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse

from .models import Pedido, ItemPedido

@csrf_exempt
def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        if not usuario or not senha:
            messages.error(request, "Preencha todos os dados.")
            return render(request, 'login.html')

        
        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Sua conta está desativada.")
        else:
            messages.error(request, "Credenciais inválidas. Tente novamente.")
        

    return render(request, 'login.html')


@login_required
def home(request):
    pedidos = Pedido.objects.all().order_by('-data')

    status_filtro = request.GET.get('status')
    if status_filtro:
        pedidos = pedidos.filter(status=status_filtro)
    
    busca = request.GET.get('busca')
    if busca:
        pedidos = pedidos.filter(id=busca)

    contexto = {
        'pedidos': pedidos,
    }

    return render(request, 'home.html', contexto)


@login_required
def detalhar_pedido(request, pedido_id):

    pedido = get_object_or_404(Pedido, id=pedido_id)
    contexto = {
        'pedido': pedido
    }
    return render(request, 'detalhe_pedido.html', contexto)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# pedidos
@csrf_exempt
@login_required
def criar_pedido(request):
    if request.method == 'POST':
        novo = Pedido.objects.create()
        return JsonResponse({'id': novo.id, 'status': novo.status})

@csrf_exempt
def fechar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    if not pedido.itens.exists():
        return JsonResponse({'error': 'Não pode fechar pedido sem itens'}, status=400)

    pedido.status = "FECHADO"
    pedido.save()
    return JsonResponse({'sucess' :True, 'status': "FECHADO"})

@csrf_exempt
@login_required
def cancelar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    pedido.status = 'CANCELADO'
    pedido.save()
    return JsonResponse({'sucess': True, 'status': "CANCELADO"})

@login_required
def listar_pedidos(request):
    status_filtro = request.GET.get('status')
    busca_id = request.GET.get('busca')
    
    pedidos = Pedido.objects.all().order_by('-data')
    
    if status_filtro:
        pedidos = pedidos.filter(status=status_filtro)
    if busca_id:
        pedidos = pedidos.filter(id=busca_id)
        
    lista_final = []
    for p in pedidos:
        lista_final.append({
            'id': p.id,
            'data': p.data.strftime('%d/%m/%Y %H:%M'),
            'status': p.status,
            'total': float(p.total)
        })
        
    return JsonResponse(lista_final, safe=False)