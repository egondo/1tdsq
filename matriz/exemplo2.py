matriz = []

i = 0
while i < 4:
    matriz.append([0] * 5)
    i = i + 1

num = 1
for i in range(4):
    for j in range(5):
        matriz[i][j] = num
        num = num + 1

for linha in matriz:
    print(linha)