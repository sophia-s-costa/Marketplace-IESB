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
Criar um pedido (logado, por exemplo pela API navegável em /api/pedidos/):
{
  "itens": [
    { "produto": 1, "quantidade": 2 }
  ]
}
## Prints
<img width="1056" height="492" alt="image" src="https://github.com/user-attachments/assets/dddb262e-ef72-4750-9bc0-b9432ea3e7ff" />
<img width="1056" height="492" alt="image" src="https://github.com/user-attachments/assets/a7296e9a-88a1-4472-8d8e-3a48949b7dac" />
<img width="1578" height="590" alt="image" src="https://github.com/user-attachments/assets/3fc4df0e-fa94-491e-8173-a10861e937ba" />



## Autor
Sophia Silva — IESB 2026
