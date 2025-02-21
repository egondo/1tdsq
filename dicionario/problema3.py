def menu() -> int:
    print("1 - Insere\n2 - Altera\n3 - Consulta\n4 - Apaga\n5 - Sair")
    return int(input("Opção: "))

def get_produto() -> dict:
    cod = int(input("Código: "))
    desc = input("Descrição: ")
    qtd = int(input("Quantidade: "))
    prc = float(input("Preço: "))
    prod = {'codigo': cod, 'descricao': desc, 'quantidade': qtd, 'preco': prc}
    return prod

def busca(lista: list, codigo: int) -> int:
    i = 0
    while i < len(lista) and lista[i]['codigo'] != codigo:
        i = i + 1

    if i == len(lista):
        return -1
    else:
        return i

if __name__ == "__main__":
    banco = []
    opcao = menu()
    while opcao != 5:
        if opcao == 1:
            prod = get_produto()
            pos = busca(banco, prod['codigo'])
            if pos == -1:
                banco.append(prod)
            else:
                print(f"Já existe produto com código {prod['codigo']}")
                
        elif opcao == 2:
            prod = get_produto()
            #procurar o produto cujo codigo é igual a prod['codigo']
            #fazer as alteracoes se ele existir no dicionario
            pos = busca(banco, prod['codigo'])
            if pos == -1:
                print(f"Código: {prod['codigo']} não existe!")
            else:
                banco[pos] = prod
        elif opcao == 4:
            cod = int(input("Informe o código: "))
            pos = busca(banco, cod)
            if pos == -1:
                print("Produto não encontrado!")
            else:
                banco.pop(pos)
                print("Produto excluído com sucesso!")
        elif opcao == 3:
            cod = int(input("Informe o código: "))
            pos = busca(banco, cod)
            if pos == -1:
                print("Não existe produto com tal codigo")
            else:
                print(banco[pos])

        opcao = menu()
