from django.db import models
from django.core.exceptions import ValidationError


STATUS_PEDIDOS = [
    ("RASCUNHO", "Rascunho"),
    ("FECHADO", "Fechado"),
    ("CANCELADO", 'Cancelado'),
]

class Pedido(models.Model):
    data = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_PEDIDOS, default='RASCUNHO')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Pedido #{self.id} - {self.status}"

    def atualizar_total(self):
        total_calculado = sum(item.subtotal for item in self.itens.all())
        self.total = total_calculado
        self.save()


class ItemPedido(models.Model):

    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    descricao = models.TextField()
    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.descricao

    def save(self, *args, **kwargs):
        if self.quantidade <= 0:
            raise ValidationError("A quantidade deve ser maior que zero")

        self.subtotal = self.quantidade * self.valor_unitario

        super().save(*args, **kwargs)

        self.pedido.atualizar_total()

    def delete(self, *arg, **kwargs):
        pedido = self.pedido
        super().delete(*args, **kwargs)
        pedido.atualizar_total()