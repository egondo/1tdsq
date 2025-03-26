import oracledb

conexao = oracledb.connect(user="pf0313", 
                           password="professor#23",
                           dsn="oracle.fiap.com.br/orcl")

ins = '''insert into TB_filme(titulo, data_lancamento, diretor, atores, nota) 
          values(:titulo, to_date(:data_lancamento, 'YYYY-MM-DD'), :diretor, 
          :atores, :nota)'''

filme = {
    "titulo": "I'm still here",
    "data_lancamento": "2024-05-10",
    "diretor": "Walter Salles",
    "atores": "Fernanda Torres, Fernanda Montenegro e Selton Mello",
    "nota": 8.4
}

cursor = conexao.cursor()
cursor.execute(ins, filme)
conexao.commit()
print("Filme incluido com sucesso!")

cursor.close()
conexao.close()