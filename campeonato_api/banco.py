import oracledb

def get_conexao():
    con = oracledb.connect(user="pf0313", password="professor#23",
                          dsn="oracle.fiap.com.br/orcl")

    return con

#Os times serao cadastrados antes das partidas
def insere_time(time: dict):
    ins = "insert into t_time(nome) values(:nome)"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(ins, time)
        con.commit()


def insere_lista_times(lista_times: list):
    ins = "insert into t_time(nome) values(:nome)"
    with get_conexao() as con:
        with con.cursor() as cur:
            #cur.executemany(ins, lista_times)
            for item in lista_times:
                cur.execute(ins, item)
        con.commit()

def insere_partida(partida: dict):
    ins = "insert into t_partida(id_mandante, id_visitante, local, gols_mandante, gols_visitante, data) values(:casa, :visitante, :local, :gcasa, :gvisitante, to_date(:data, 'DD/MM/YYYY HH24:MI'))"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(ins, partida)
        con.commit()

def altera_time(time: dict):
    upt = "update t_time set nome=:nome, vitorias=:vitorias, empates=:empates, derrotas=:derrotas, gols_marcados=:gols_marcados, gols_sofridos=:gols_sofridos where id = :id"

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(upt, time)
        con.commit()

def recupera_time_id(id: int):
    sel = "select id, nome, vitorias, derrotas, empates, gols_marcados, gols_sofridos from t_time where id = :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sel, {"id": id})
            dados = cur.fetchone()
    time = {
        "id": dados[0],
        "nome": dados[1],
        "vitorias": dados[2],
        "derrotas": dados[3],
        "empates": dados[4],
        "gols_marcados": dados[5],
        "gols_sofridos": dados[6]
    }
    return time


