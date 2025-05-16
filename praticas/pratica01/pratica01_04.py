'''
4. Calculadora de Preço Total
- Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:
  - Nome do produto: "Cadeira Infantil"
  - Preço unitário: R$ 12.40
  - Quantidade: 3
  > O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
'''

NOME_PRODUTO="Cadeira Infantil"
PRECO_UNITARIO=12.40
QUANTIDADE=3
print(f"Nome do produto: {NOME_PRODUTO}")
print(f"Preço unitário: R$ {PRECO_UNITARIO}")
print(f"Quantidade: {QUANTIDADE}")
print(f"Preço unitário: R$ {PRECO_UNITARIO}")
CARACTERE = "-"
SEPARADOR = CARACTERE * 40
print(SEPARADOR)
print(f"Preço total: R$ {PRECO_UNITARIO * QUANTIDADE}")