import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23", 
                            dsn="oracle.fiap.com.br/orcl")

def recupera_perguntas(enquete_id: int) -> list:
    sql = "select p.id, p.numero, p.questao, p.tipo, i.nome from tb_pergunta p left join tb_item i on p.id = i.pergunta_id where enquete_id = :enquete order by p.numero"
    with get_conexao() as con:
        with con.cursor() as cur:

            param = {"enquete": enquete_id}
            
            cur.execute(sql, param)
            dados = cur.fetchall()
            return dados
        
if __name__ == "__main__":
    registros = recupera_perguntas(1)
    for pergunta in registros:
        print(pergunta)