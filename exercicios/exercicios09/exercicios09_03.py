""" EXERCICIOS 09 - 03 senha forte

Crie um programa que verifique se uma senha é forte. 
Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número.
O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
"""
def eh_senha_forte(senha):
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True
# Testando a função
while True:
    print("Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número.")
    senha = input("Digite uma senha (ou 'sair' para sair): ")
    if senha.lower() == 'sair':
        break
    if eh_senha_forte(senha):
        print("Senha forte!")
    else:
        print("Senha fraca!")


    