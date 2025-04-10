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
            c['id'] = new_id.getvalue()[0]
        con.commit()


def insere_venda(venda: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            ins = "insert into t_venda(id, data, valor, id_cliente) values(gerador.nextval, to_date(:data, 'DD-MM-YYYY'), :valor, :id_cliente) returning id into :id"

            new_id = cur.var(oracledb.NUMBER)
            venda['id'] = new_id
            print(f'venda {venda}')
            cur.execute(ins, venda)
            venda['id'] = new_id.getvalue()[0]
        con.commit()

def insere_itemvenda(item: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            ins = "insert into t_itemvenda(produto, quantidade, valor, id_venda) values(:produto, :quantidade, :valor, :id_venda)"
            cur.execute(ins, item)
        con.commit()        


def recupera_cliente_documento(documento):
    return None

if __name__ == "__main__":
    cliente = {
        "nome": "Joao Alvares",
        "email": "joaoalvares@gmail.com",
        "documento": "234.828.902-00"
    }

    insere_cliente(cliente)

    print(cliente)