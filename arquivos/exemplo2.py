import random

times = ["São Paulo", "Palmeiras", "Portuguesa", "Corinthians", "Juventus", "Nacional"]

with open("arquivos/resultados.txt", mode="w") as arq:
    for i in range(len(times)):
        for j in range(i + 1, len(times)):
            g1 = random.randint(0, 5)
            g2 = random.randint(0, 5)
            info = f"{times[i]} {g1} X {g2} {times[j]}"
            arq.write(info)
            arq.write("\n")

    for i in range(len(times)):
        for j in range(i + 1, len(times)):
            g1 = random.randint(0, 5)
            g2 = random.randint(0, 5)
            info = f"{times[i]} {g1} X {g2} {times[j]}"
            arq.write(info)
            arq.write("\n")