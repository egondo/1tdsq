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
        i = 10
        if i < len(lista):
            print(lista[i])
        else:
            print("Posição inválida")

        arq = open("excecoes/exemplo.py", mode="r")
        print(arq.read())
        arq.close()
    except:
        print("Aconteceu um erro! Contate a TI e informe o erro gerado!")    
