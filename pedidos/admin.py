from django.contrib import admin
from .models import Pedido, ItemPedido
# Register your models here.


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'status', 'total')
    list_filter = ('status',)
    inlines = [ItemPedidoInline]