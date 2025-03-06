import json

arquivo = open("dados.txt", mode="r", encoding="utf8")
dado = json.load(arquivo)
print(dado)

