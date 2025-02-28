with open("arquivos/dados.txt", "r") as arq:
    dados = arq.read()
print(dados )

arq = open("arquivos/dados.txt", "r")
dados = arq.read()
arq.close()
print(dados)