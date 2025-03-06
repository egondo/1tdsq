import json
import traceback

def menu():
    print("1) cadastra")
    print("2) consulta")
    print("3) sair")
    opcao = int(input("Opcao: "))
    return opcao

def leitura_arquivo() -> dict:
    #print("Lendo arquivo")
    try:
        with open("d:/pix.dat", mode="r", encoding="utf8") as arq:
            retorno = json.load(arq)
            return retorno
    except Exception:
        traceback.print_exc()
        return {}  #retornando um dicionario vazio

def cadastro(info: dict):
    #print("cadastrando info PIX")
    chave = input("Informe chave pix: ")
    if chave in info:
        print("Chave existente!")
    else:
        nome = input("Nome: ")
        doc = input("Documento: ")
        banco = input("Banco: ")
        conta = input("Conta: ")

        valor = {"nome": nome, "doc": doc, "banco": banco, "conta": conta}
        
        info[chave] = valor

def consulta(info: dict) -> object:
    #print("Fazendo a consulta")
    chave = input("chave pix: ")
    if chave in info:
        return info[chave]
    else:
        return "Nenhuma informacao encontrada"

def gravacao_arquivo(info: dict):
    #print("Gravando arquivos")
    with open("d:/pix.dat", mode="w", encoding="utf8") as arq:
        json.dump(info, arq, indent=2)

if __name__ == "__main__":
    print("SISTEMA CHAVE PIX")
    escolha = menu()
    dados = leitura_arquivo()
    while escolha != 3:
        if escolha == 1:
            cadastro(dados)
        elif escolha == 2:
            resultados = consulta(dados)
            print(resultados)
        elif escolha != 3:
            print("Opção inválida!")
    
        escolha = menu()
    
    print(dados)
    gravacao_arquivo(dados)