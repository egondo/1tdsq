def inverte(dicionario: dict) -> dict:
    dic_invertido = {}

    for chave in dicionario:
        valor = dicionario[chave]
        dic_invertido[valor] = chave
    
    return dic_invertido

disciplinas = {}
disciplinas['Algoritmos'] = 'Computational Thinking in Python'
disciplinas['Desenvolvimento WEB'] = 'Front-end and design Web'
disciplinas['Programação Orientada a Objetos'] = 'DDD'

disc_invertido = inverte(disciplinas)

for k in disc_invertido.keys():
    print(f'{k} => {disc_invertido[k]}')