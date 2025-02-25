if __name__ == "__main__":

    try:
        nome = input("Informe o nome: ")
        dia_nascimento = int(input("Dia do nascimento: "))

        print(f"{nome} nasceu no dia {dia_nascimento}")
        
        num_a = float(input("A: "))
        num_b = float(input("B: "))
        divisao = num_a / num_b
        print(f"{num_a}/{num_b} = {divisao}")

        lista = ["Ana", "Bia", "Carol", "Duda"]
        i = 3
        print(lista[i])

        arq = open("excecoes/exemplo.py", mode="r")
        print(arq.read())
        arq.close()

    except ValueError:
        print("Erro na conversao dos dados! Digite número válido")
    except PermissionError:
        print("Vc nao tem permissao para ler o arquivo")
    except FileNotFoundError:
        print("Arquivo nao existe")
    except IndexError:
        print("Acesso inválido a um indice da lista")
    except:
        print("Aconteceu um erro! Contate a TI e informe o erro gerado!")    
