from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .models import ItemPedido, Pedido, Produto


def catalogo(request):
    return render(request, 'loja/catalogo.html')
@require_POST

def adicionar_ao_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    chave = str(produto_id) # chaves de sessão (JSON) precisam ser texto
    carrinho[chave] = carrinho.get(chave, 0) + 1
    request.session['carrinho'] = carrinho
    request.session.modified = True # avisa o Django que o dict interno mudou
    if request.headers.get('x-requested-with') == 'fetch':
        return JsonResponse({'itens': sum(carrinho.values())})
    messages.success(request, 'Produto adicionado ao carrinho.')

    return redirect('carrinho')
def _montar_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    produtos = Produto.objects.filter(pk__in=[int(k) for k in carrinho])
    itens, total = [], Decimal('0')
    for produto in produtos:
        qtd = carrinho[str(produto.pk)]
        subtotal = produto.preco * qtd
        total += subtotal
        itens.append({'produto': produto, 'quantidade': qtd, 'subtotal': subtotal})
    return itens, total
def ver_carrinho(request):
    itens, total = _montar_carrinho(request)
    return render(request, 'loja/carrinho.html', {'itens': itens, 'total': total})

@login_required
@require_POST
def finalizar_compra(request):
    carrinho = request.session.get('carrinho', {})
    if not carrinho:
        messages.warning(request, 'Seu carrinho está vazio.')
        return redirect('carrinho')

    try:
        with transaction.atomic():
            produtos = Produto.objects.select_for_update().filter(
                pk__in=[int(k) for k in carrinho]
            )
            por_id = {p.pk: p for p in produtos}

            # 1) Valida o estoque de TODOS os itens antes de gravar qualquer coisa.
            for chave, qtd in carrinho.items():
                produto = por_id.get(int(chave))
                if produto is None or produto.estoque < qtd:
                    nome = produto.nome if produto else f'#{chave}'
                    raise ValueError(f'Estoque insuficiente para "{nome}".')

            # 2) Cria pedido e itens, copia o preço atual e baixa o estoque.
            pedido = Pedido.objects.create(comprador=request.user)
            for chave, qtd in carrinho.items():
                produto = por_id[int(chave)]
                ItemPedido.objects.create(
                    pedido=pedido,
                    produto=produto,
                    quantidade=qtd,
                    preco_unitario=produto.preco,
                )
                Produto.objects.filter(pk=produto.pk).update(
                    estoque=F('estoque') - qtd
                )
    except ValueError as erro:
        messages.error(request, f'{erro} Nenhum item foi comprado.')
        return redirect('carrinho')

    request.session['carrinho'] = {}  # só limpa depois do sucesso
    messages.success(request, f'Pedido #{pedido.pk} realizado com sucesso!')
    return redirect('catalogo')