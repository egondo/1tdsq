import requests

cep =  "01209000"
url = f"https://viacep.com.br/ws/{cep}/json"

objeto = requests.get(url) #retorna um objeto e não o json ainda
#print(objeto)
if objeto.status_code == 200:
    info = objeto.json()
    print(info)
elif objeto.status_code == 400:
    print("Erro 400, verifique o cep informado!")
else:
    print(objeto.status_code)



