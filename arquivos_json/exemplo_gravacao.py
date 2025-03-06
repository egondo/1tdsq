import json

livro = {
    "titulo": "Harry Potter e a Pedra Filosofal",
    "autor": "J. K. Rolling",
    "ano": 1997,
    "original": "Harry Potter and Phillosopher's Stone",
    "generos": ["ficção", "infantil", "drama"]
}

arquivo = open("dados.txt", mode="w", encoding="utf8")
json.dump(livro, arquivo, indent=4)
arquivo.close()
print("Programa finalizado")
