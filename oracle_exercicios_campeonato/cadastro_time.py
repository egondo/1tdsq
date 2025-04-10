import banco
import datetime

times = ["Palmeira", "Corinthians", "Cruzeiro", "Coritiba", "Chapecoense", "Criciúma", "Caxias do Sul", "Ponte Preta", "Portuguesa", "Taubaté", "Tatuapé", "Tolima", 'Torino', 'Tocantins']

ini = datetime.datetime.now()
lista = []
for nome in times:
    time = {"nome": nome}
    lista.append(time)
    #banco.insere_time(time)

banco.insere_lista_times(lista)
fim = datetime.datetime.now()
print(f"{fim} : {ini}")