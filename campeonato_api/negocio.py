import banco

def recupera_times():
    return banco.recupera_todos_times()


def cadastra_partida(partida: dict):
    id_casa = partida['casa']
    id_visitante = partida['visitante']
    time_casa = banco.recupera_time_id(id_casa)
    time_visitante = banco.recupera_time_id(id_visitante)

    if partida['gcasa'] > partida['gvisitante']:
        time_casa['vitorias'] = time_casa['vitorias'] + 1
        time_visitante['derrotas'] = time_visitante['derrotas'] + 1
    elif partida['gcasa'] < partida['gvisitante']:
        time_casa['derrotas'] = time_casa['derrotas'] + 1
        time_visitante['vitorias'] = time_visitante['vitorias'] + 1
    else:
        time_casa['empates'] = time_casa['empates'] + 1
        time_visitante['empates'] = time_visitante['empates'] + 1

    time_casa['gols_marcados'] = time_casa['gols_marcados'] + partida['gcasa']
    time_casa['gols_sofridos'] = time_casa['gols_sofridos'] + partida['gvisitante']

    time_visitante['gols_marcados'] = time_visitante['gols_marcados'] + partida['gvisitante']
    time_visitante['gols_sofridos'] = time_visitante['gols_sofridos'] + partida['gcasa']

    banco.altera_time(time_casa)
    banco.altera_time(time_visitante)
    banco.insere_partida(partida)