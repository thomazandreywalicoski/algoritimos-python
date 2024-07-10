notas = []

def ler_nota():
    notas.append(float(input("Digite uma nota: ")))

def calcular_media():
    soma = sum(notas)
    print("A soma foi:", soma)
    quantidade_notas = len(notas)
    media = soma / quantidade_notas
    print("A média foi:", media)

ler_nota()
ler_nota()
ler_nota()

maior_nota = max(notas)
menor_nota = min(notas)

print(f"A maior nota foi: {maior_nota}")
print(f"A menor nota foi: {menor_nota}")

calcular_media()

