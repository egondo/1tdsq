def coloca_espaco(palavra: str) -> str:
    resp = ''
    for letra in palavra:
        #print(letra)
        resp = resp + letra + ' '
    
    return resp

x = coloca_espaco('manga')
print(x)