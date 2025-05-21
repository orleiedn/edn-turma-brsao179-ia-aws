""" Exercicio 03.04

Crie um programa que solicite ao usuário que insira números inteiros. 

- O programa deve continuar solicitando números até que o usuário digite 'fim'.
- Para cada número inserido, o programa deve informar se é par ou ímpar.
- Se o usuário inserir algo que não seja um número inteiro, o programa deve informar o erro e continuar.
- No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.
"""
pares = 0
impares = 0
while True:
    try:
        numero = input("Digite um número inteiro (ou 'fim' para encerrar): ")
        if numero.lower() == 'fim':
            break
        numero = int(numero)
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
    except Exception as e:
        print(f"Erro inesperado: {e}. Tente novamente.")

print(f"Quantidade de numeros pares é = {pares}.")
print(f"Quantidade de numeros ímparres é = {impares}.")
