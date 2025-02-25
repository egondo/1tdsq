import traceback
if __name__ == "__main__":

    try:
        arq = open("excecoes/exemplo1.py", mode="r")
        conteudo = arq.read()
        arq.close()
    except:
        print("Algo deu errado no acesso do arquivo")
        print("Envie o erro abaixo para profeduardo@fiap.com.br")
        traceback.print_exc()

    else:
        print(conteudo)
    
