# Marketplace Simplificado — Projeto 5
Marketplace em Django: vendedores cadastram produtos, compradores
navegam pelo catálogo, usam o carrinho e finalizam pedidos.
## Funcionalidades

IESB • Construção de Backend • Projeto 5 • Guia do Aluno • Página 21
- Admin com isolamento: cada vendedor vê só os próprios produtos
- Carrinho na sessão (funciona sem login)
- Checkout atômico: pedido, itens e baixa de estoque, tudo ou nada
- Preço histórico em cada item do pedido
- API REST: produtos (leitura pública) e pedidos (serializer aninhado)
- Catálogo com fetch() e contador em localStorage
## Como rodar
1. python -m venv venv e ative o ambiente
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver
## Exemplo de chamada à API
(cole aqui o JSON enviado em /api/pedidos/ e a resposta)
## Prints
(catálogo, carrinho, Admin do vendedor)
## Autor
Sophia Silva — IESB 2026