# PRATICA 02 - Inteligencia Artificla
""" 3. Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

"""
nota_1 = 7.5
nota_2 = 8.0
nota_3 = 6.5
media = (nota_1 + nota_2 + nota_3) / 3
print(f"Nota 1: {nota_1:.2f}")
print(f"Nota 2: {nota_2:.2f}")
print(f"Nota 3: {nota_3:.2f}")
print(f"Média: {media:.2f}")
if media >= 7:
    print("Resultado: Aprovado")
elif media >= 5:
    print("Resultado: Recuperação")
else:
    print("Resultado: Reprovado")
# Fim do código