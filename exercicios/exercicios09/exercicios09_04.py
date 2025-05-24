""" EXERCICIOS 09 - 04
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""
def calcular_idade_em_dias(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade * 365
# Testando a função
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_em_dias = calcular_idade_em_dias(ano_nascimento)
print(f"A idade em dias é: {idade_em_dias} dias")
    