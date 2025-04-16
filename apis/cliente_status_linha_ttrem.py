import requests

url = 'https://www.diretodostrens.com.br/api/status'
objeto = requests.get(url) #retorna um objeto e não o json ainda
#print(objeto)
if objeto.status_code == 200:
    info = objeto.json()
    #print(info) #-> info é um dicionário ou uma lista de dicionários
    for linha in info:
        if linha['situacao'] != 'Operação Normal':
            print(f"Número da linha: {linha['codigo']} -> {linha['situacao']}")

elif objeto.status_code == 400:
    print("Erro 400, verifique o cep informado!")
else:
    print(objeto.status_code)



