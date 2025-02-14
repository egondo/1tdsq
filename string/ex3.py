def substitui(frase: str, letra: str) -> str:
    resp = ''
    for c in frase:
        if c.lower() == letra.lower():
            resp = resp + '*'
        else:
            resp = resp + c
    return resp

valor = substitui('JabuticaBA', 'a')
print(valor)

