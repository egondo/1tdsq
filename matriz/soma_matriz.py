def soma(mat_a: list, mat_b: list) -> list:
    lin_a = len(mat_a)
    col_a = len(mat_a[0])
    lin_b = len(mat_b)
    col_b = len(mat_b[0])

    #verificacao se é possíve efetuar a soma
    if lin_a != lin_b or col_a != col_b:
        raise Exception("Impossível somar, dimensões diferente")
    
    #criando a matriz soma (resultado), tudo preenchido com 0
    resultado = []
    for i in range(lin_a):
        resultado.append([0] * col_a)

    #Efetuar a soma das matrizes
    for i in range(lin_a):
        for j in range(col_a):
            resultado[i][j] = mat_a[i][j] + mat_b[i][j]

    return resultado

if __name__ == "__main__":
    a = [
        [2, 5, 6, 8],
        [-1, 3, -8, 0]
    ]

    b = [
        [-1, 2, 3],
        [0, -1, 4]
    ]

    try:
        resp = soma(a, b)

        for lin in resp:
            print(lin)
    except Exception as e:
        print(e)