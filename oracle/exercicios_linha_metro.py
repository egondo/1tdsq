import oracledb
'''create table t_linha(
    id number generated as identity,
    nome varchar2(100),
    numero number(3),
    tipo varchar2(50),
    operador varchar2(50),
    inicio varchar2(100),
    fim varchar2(100),
    extensao number(8,2),
    primary key(id));
    '''
def get_conexao():
    return oracledb.connect(user="pf0313", 
                            password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")

def insere_linha(linha: dict):
    ins = "INSERT INTO t_linha(nome, numero, tipo, inicio, fim, extensao, operador) values(:nome, :numero, :tipo, :inicio, :fim, :extensao, :operador)"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(ins, linha)
        conn.commit()

if __name__ == "__main__":
    '''esmeralda = {
        "nome": "esmeralda",
        "numero": 9,
        "tipo": "trem",
        "inicio": "Osasco",
        "fim": "Varginha",
        "operador": "CCR",
        "extensao": 37.3
    }'''        

    azul = {
        "nome": "azul",
        "numero": 1,
        "tipo": "metrô",
        "inicio": "Jabaquara",
        "fim": "Tucuruvi",
        "operador": "METRO",
        "extensao": 20.2
    }
    insere_linha(azul)