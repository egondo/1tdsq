'''Suponha que temos 3 lojas que comercializa alguns produtos:
celular, smart tv, notebook, geladeira e m´aquina de lavar. Sua
tarefa ´e gerar um arquivo txt contendo o faturamento anual
(2022) das trˆes lojas. Use a biblioteca random para isso. O
arquivo dever´a ter o seguinte formato:
<produto>;<marca>;<loja>;<data>;<qtd>;<valor unit´ario>
Use o ; como separador dos campos e o seu arquivo precisa
conter, pelo menos, 5 mil entradas. Como sugest˜ao, utilize
listas e dicion´arios para representar as lojas, os produtos e suas
respectivas marcas (use 2 para cada produto) e os respectivos
valores para elas. Creio que dessa forma ficar´a mais f´acil para
criar os registros a serem gravados nos arquivos.'''

import random

def retorna_produto():
    prod = ["celular", "smart tv", "notebook", 'geladeira', 'lavadora']
    pos = random.randint(0, len(prod) - 1)
    return prod[pos]


def retorna_marca():
    marca = ["samsung", "lg", "asus", "panasonic", "sony", "electrolux"]
    pos = random.randint(0, len(marca) - 1)
    return marca[pos]

def amanha(data: str) -> str:
    campos = data.split("/")
    dia = int(campos[0])
    mes = int(campos[1])
    dia = dia + 1
    if dia >= 29:
        dia = 1
        mes = mes + 1
    return f"{dia}/{mes}/{campos[2]}"

if __name__ == "__main__":
    lojas = ["Plaza Sul", "Cid SP", "Sta Cruz"]
    data = "2/1/2022"
    with open('faturamento_anual.txt', mode="w") as arq:
        while data != "28/12/2022":
            for i in range(6):
                prod = retorna_produto()
                marca = retorna_marca()
                for loja in lojas:
                    qtd = random.randint(3, 70)
                    preco = random.randint(1500, 7000) + random.randint(0, 99) / 100.0
                    lin = f"{prod};{marca};{loja};{data};{qtd};{preco}"
                    arq.write(lin + "\n")
            data = amanha(data)



