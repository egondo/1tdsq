frase = input("Informe a frase/palavra: ").lower()

contador = {}

for letra in frase:
    if letra in contador:
        contador[letra] = contador[letra] + 1
    else:
        contador[letra] = 1

for key in contador.keys():
    print(f'{key} - {contador[key]}')
