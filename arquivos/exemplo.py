import random

disc = ["CTP", "IA", "DDD", "Software Design", "BD", "Frontwend"]

pos = random.randint(0, len(disc) - 1)

nota = int(random.random() * 100) / 10.0

print(f"Minha nota de {disc[pos]} foi {nota}")