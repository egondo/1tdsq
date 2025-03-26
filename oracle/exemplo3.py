import oracledb

con = oracledb.connect(user="pf0313", password="professor#23",
                       dsn="oracle.fiap.com.br/orcl")

upd = "update tb_filme set sinopse=:sino, estudio=:estudio where id=:id"

cursor = con.cursor()

dado = {
    "sino": '''Conta a vida da Eunice Paiva após o desaparecimento 
            do seu marido, o deputado Paiva. O filme é baseado no livro
            de um dos seus filhos, o escrito Marcelo Rubens Paiva.''',
    "estudio": "Universal",
    "id": 22
}
cursor.execute(upd, dado)
con.commit()
cursor.close()
con.close()