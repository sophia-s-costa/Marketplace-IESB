from django.urls import path

from . import api_views, views

urlpatterns = [
    # Páginas (templates)
    path('', views.catalogo, name='catalogo'),
    path('carrinho/', views.ver_carrinho, name='carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho,
        name='adicionar_carrinho'),
    path('checkout/', views.finalizar_compra, name='checkout'),

    # API (DRF)
    path('api/produtos/', api_views.ProdutoListCreateView.as_view(), name='api-produtos'),
    path('api/pedidos/', api_views.PedidoCreateView.as_view(), name='api-pedidos'),
]