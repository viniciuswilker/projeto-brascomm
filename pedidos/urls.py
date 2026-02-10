from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('pedidos/<int:pedido_id>/', views.detalhar_pedido, name='detalhe_pedido'),


    path('api/pedidos/novo/', views.criar_pedido, name='api_criar_pedido'),
    path('api/pedidos/', views.listar_pedidos, name='api_listar_pedidos'),
    
    path('api/pedidos/<int:pedido_id>/fechar/', views.fechar_pedido, name='api_fechar_pedido'),
    path('api/pedidos/<int:pedido_id>/abrir/', views.abrir_pedido, name='api_abrir_pedido'),
    path('api/pedidos/<int:pedido_id>/cancelar/', views.cancelar_pedido, name='api_cancelar_pedido'),
    
    path('api/pedido/<int:pedido_id>/itens/', views.listar_itens, name='api_listar_itens'),


    # path('api/pedidos/<int:pedido_id>/', views.detalhar_pedido, name='api_detalhar_pedido'),



    path('api/pedidos/<int:pedido_id>/itens/add/', views.adicionar_item, name='api_adicionar_item'),
    path('api/itens/<int:item_id>/remover/', views.remover_item, name='api_remover_item'),
    path('api/itens/<int:item_id>/editar/', views.editar_item, name='api_editar_item'),
    
]