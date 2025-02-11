#public String maiuscula(String palavra) {
#    return palavra.toUpperCase();
#}
def maiuscula(palavra: str) -> str:
    return palavra.upper()

resp = maiuscula("fiap")
print(resp)

resp = maiuscula('algoritmos')
print(resp)

resp = maiuscula('''python''')
print(resp)
