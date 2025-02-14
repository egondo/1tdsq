import palavras_forca

def gera_segredo(word: str, chute: str) -> str:
    resp = ""
    for c in word:
        if c.lower() in chute:
            resp = resp + c + " "
        else:
            resp = resp + "_ "
    return resp


palavra = palavras_forca.get_country()
erros = 0
chutes = ' '
segredo = gera_segredo(palavra, chutes)


while erros < 6 and '_' in segredo:
    print(segredo)
    print(f"Erros: {erros}")
    letra = input('Letra: ').lower()
    chutes = chutes + letra
    #verificar se a letra esta na palavra sorteada
    segredo = gera_segredo(palavra, chutes)
    if not letra in palavra.lower():
        erros = erros + 1

if erros >= 6:
    print(f"Você foi enforcado, a palavra era {palavra}")
else:
    print(f'Parabéns, você acerto {palavra}')