# PRATICA 02 - Inteligencia Artificla
""" 2. Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%

O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""
produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20
desconto = (preco_original * porcentagem_desconto) / 100
preco_final = preco_original - desconto
print(f"Produto: {produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Porcentagem de desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")