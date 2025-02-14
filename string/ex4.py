def substitui(frase: str, letras: str) -> str:
    resp = ''
    for c in frase:
        if c.upper() in letras.upper():
            resp = resp + '*'
        else:
            resp = resp + c
    return resp

def subst(frase: str, letras: str) -> str:
    resp = ''
    letras = letras.lower()
    for c in frase:
        if c.lower() in letras:
            resp = resp + '*'
        else:
            resp = resp + c
    return resp

valor = subst('hoje pode chover mais cedo', 'ed')
print(valor)