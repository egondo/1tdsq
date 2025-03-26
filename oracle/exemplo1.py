import oracledb

conexao = oracledb.connect(user="pf0313", 
                           password="professor#23", 
                           dsn="oracle.fiap.com.br/orcl")

print(f"Oracle conexao {conexao.version}")
cursor = conexao.cursor()

sql = "SELECT * FROM TB_CARRO"
cursor.execute(sql)
#Qual é o tipo do objeto cursor?
#Resp: cursor é um oracledb.Cursor
for reg in cursor:
    #reg é uma tupla (tuple)
    print(reg)

sql = "SELECT * FROM TB_ENQUETE"
cursor.execute(sql)
registros = cursor.fetchall()
#Qual é o tipo do objeto registros?
#uma lista de tuplas contendo o resultado da minha consulta (matriz somente leitura)
print(registros)

for reg in registros:
    print(reg)

cursor.close()
conexao.close()    