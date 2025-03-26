import oracledb

with oracledb.connect(user="pf0313", password="professor#23",
                       dsn="oracle.fiap.com.br/orcl") as con:
    with con.cursor() as cursor:
        status = "InCompleta"
        id = '21 or 1=1'
        upd = f"update tarefa set status='{status}' where id={id}"
        print(upd)
        cursor.execute(upd)
    con.commit()

#meu banco fica passível a um ataque de SQLInjection