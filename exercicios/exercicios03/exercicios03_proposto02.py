numeros = [5, 8, 3, -1, 7]
for numero in numeros:
    if numero < 0:
        print(f"{numero} invalido (é ímpar)")
        break
    if numero % 2 == 0:
        continue
    print(f"Numero, [{numero}]")
    