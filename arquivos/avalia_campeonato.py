def processa_partida(partida: str) -> list:
    #Nacional 5 X 2 Red Bull\n
    partida = partida.replace('\n', '')
    campos = partida.split(" X ")

    #'Nacional 5' -> ['Nacional', 5]
    #'2 Red Bull' -> ['Red Bull', 2]
    time_a = campos[0].split(' ')
    time_b = campos[1].split(' ')

    resultado = []
    if len(time_a) == 2:
        resultado.append(time_a[0])
        resultado.append(int(time_a[1]))
    else:
        resultado.append(f"{time_a[0]} {time_a[1]}")
        resultado.append(int(time_a[2]))

    if len(time_b) == 2:
        resultado.append(time_b[1])
        resultado.append(int(time_b[0]))
    else:
        resultado.append(f"{time_b[1]} {time_b[2]}")
        resultado.append(int(time_b[0]))
    
    return resultado    


def atualiza_tabela(time: str, pontos: int, tabela: dict):
    if time in tabela:
        tabela[time] = tabela[time] + pontos
    else:
        tabela[time] = pontos

if __name__ == "__main__":

    tabela = {}

    #encoding="ISO8859-1"
    arq = open("arquivos/resultados.txt", mode="r", encoding="utf8")
    dados = arq.readlines()
    for jogo in dados:
        result = processa_partida(jogo) 
        #['Palmeiras', 5, 'Santos', 2]
        mand = result[0]
        visi = result[2]
        if result[1] > result[3]: #mandante ganhou
            atualiza_tabela(mand, 3, tabela)
            atualiza_tabela(visi, 0, tabela)

        elif result[3] > result[1]:  #visitante ganhou
            atualiza_tabela(visi, 3, tabela)
            atualiza_tabela(mand, 0, tabela)

        else:    #empate
            atualiza_tabela(visi, 1, tabela)
            atualiza_tabela(mand, 1, tabela)

    arq.close()
    for time in tabela:
        print(f"{time} -> {tabela[time]}")