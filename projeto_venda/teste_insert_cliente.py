import oracledb

def get_conexao():
    con = oracledb.connect(user="pf0313", password="professor#23",
                           dsn="oracle.fiap.com.br/orcl")
    return con

def insere_cliente(c: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            ins = "insert into t_cliente(id, nome, email, documento) values(gerador.nextval, :nome, :email, :documento) returning id into :id"

            new_id = cur.var(oracledb.NUMBER)
            c['id'] = new_id
            cur.execute(ins, c)
            c['novo_id'] = new_id.getvalue()[0]
        con.commit()


cliente = {
    "nome": "Joao Alvares",
    "email": "joaoalvares@gmail.com",
    "documento": "234.828.902-00"
}

insere_cliente(cliente)

print(cliente)