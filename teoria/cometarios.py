#Esse eh um comentario de uma linha

"""_summary_
Esse eh um comentario de mais de uma linha
"""

def calcular_media(numeros):
    """
    Essa funcao calcula a media de uma lista de numeros.
    
    Args:
        numeros (list): Uma lista de numeros.
    
    Returns:
        float: A media dos numeros.
    """
    return sum(numeros) / len(numeros)
"""Exemplo de uso
numeros = [1, 2, 3, 4, 5]
media = calcular_media(numeros)
print(f"A media dos numeros {numeros} eh {media}")
"""