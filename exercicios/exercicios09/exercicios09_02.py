""" EXERCICIOS 09 - 02 palíndromo

Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, 
ignorando espaços e pontuação).

    Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”
"""
def eh_palindromo(texto):
    # Remove espaços e pontuação
    texto = ''.join(e for e in texto if e.isalnum()).lower()
    # Verifica se o texto é igual ao seu reverso
    return texto == texto[::-1]
# Testando a função
texto = input("Digite uma palavra ou frase: ")
if eh_palindromo(texto):
    print("Sim")
else:
    print("Não")
# Testando a função com exemplos
# Frases para testar  palindromo
print(eh_palindromo("Ara na ra"))  # True
print(eh_palindromo("A mala nada na lama"))
print(eh_palindromo("A torre da derrota"))
print(eh_palindromo("A cara rajada da cara"))
 