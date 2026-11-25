from django.contrib import admin
from .models import Categoria, ItemPedido, Pedido, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nome',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'estoque', 'vendedor')
    list_filter = ('categoria',)
    search_fields = ('nome',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Cada vendedor enxerga apenas os próprios produtos.
        return qs.filter(vendedor=request.user)

    def get_exclude(self, request, obj=None):
        # O vendedor comum não escolhe o dono: é sempre ele mesmo.
        return None if request.user.is_superuser else ('vendedor',)

    def save_model(self, request, obj, form, change):
        # Produto novo sem vendedor definido: o dono é o próprio usuário.
        if not change and not obj.vendedor_id:
            obj.vendedor = request.user
        super().save_model(request, obj, form, change)


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ('preco_unitario',)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'comprador', 'status', 'criado_em')
    list_filter = ('status',)
    inlines = [ItemPedidoInline]