from time import sleep

print("PROGRAMA PARA CALCULAR A MÉDIA DE UM ALUNO")
print("-" * 50)
        
nome = str(input("Digite o Nome do Aluno: "))

n1 = float(input("\nDigite a Primeira Nota: "))
while n1 < 0 or n1 > 10:
    print("Favor digitar uma nota de 0 a 10!")
    n1 = float(input("\nDigite a Primeira Nota: "))

n2 = float(input("Digite a Segunda Nota: "))
while n2 < 0 or n2 > 10:
    print("Favor digitar uma nota de 0 a 10!")
    n2 = float(input("\nDigite a Segunda Nota: "))

n3 = float(input("Digite a Terceira Nota: "))
while n3 < 0 or n3 > 10:
    print("Favor digitar uma nota de 0 a 10!")
    n3 = float(input("\nDigite a Terceira Nota: "))

n4 = float(input("Digite a Quarta Nota: "))
while n4 < 0 or n4 > 10:
    print("Favor digitar uma nota de 0 a 10!")
    n4 = float(input("\nDigite a Quarta Nota: "))

print("\nCALCULANDO A MÉDIA...")
sleep(2)

media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    situacao = "APROVADO!"
elif media < 7:
    situacao = "REPROVADO!"

print(f"\nA Média do aluno {nome} foi {media} e está {situacao}")

