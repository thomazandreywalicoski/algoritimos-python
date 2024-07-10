import random

matriz = [[0,0,0],[0,0,0],[0,0,0]]
print(matriz)

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = random.randint(0,50)

print(matriz)