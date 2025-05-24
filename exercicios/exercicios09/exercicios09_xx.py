"""_summary_
criar 3 funcoes lambdas para converter celsius para fahrenheit, fahrenheit para kelvin e kelvin para celsius  
usuario deve informar a temperatura e a escala de origem e a funcao deve retornar a temperatura convertida para a escala de destino
"""
converter_celsius_para_fahrenheit = lambda c: (c * 9/5) + 32
converter_celsius_para_kelvin = lambda c: c + 273.15
converter_fahrenheit_para_kelvin = lambda f: (f - 32) * 5/9 + 273.15
converter_fahrenheit_para_celsius = lambda f: (f - 32) * 5/9
converter_kelvin_para_celsius = lambda k: k - 273.15
converter_kelvin_para_fahrenheit = lambda k: (k - 273.15) * 9/5 + 32
def converter_temperatura():
    escala_origem = input("Qual a escala de origem? (C)elsius, (F)ahrenheit, (K)elvin): ").strip().upper()
    escala_destino = input("Qual a escala de destino? (C)elsius, (F)ahrenheit, (K)elvin): ").strip().upper()
    temperatura = float(input("Informe a temperatura: "))
    conversao = 0 
    if escala_origem == "C" and escala_destino == "F":
        conversao = converter_celsius_para_fahrenheit(temperatura)
    elif escala_origem == "C" and escala_destino == "K":
        conversao = converter_celsius_para_kelvin(temperatura)
    elif escala_origem == "F" and escala_destino == "C":
        conversao = converter_fahrenheit_para_celsius(temperatura)
    elif escala_origem == "F" and escala_destino == "K":
        conversao = converter_fahrenheit_para_kelvin(temperatura)
    elif escala_origem == "K" and escala_destino == "C":
        conversao = converter_kelvin_para_celsius(temperatura)
    elif escala_origem == "K" and escala_destino == "F":
        conversao = converter_kelvin_para_fahrenheit(temperatura)
    else:
        print("Escala de origem invalida")
    
    print(f"{temperatura}°{escala_origem} é igual a {conversao}°{escala_destino}")

if __name__ == "__main__":
    converter_temperatura()  # chamando a funcao converter_temperatura() para iniciar