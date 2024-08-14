num_escolhido = int(input("Digite a posição do número na sequência de Fibbonacci que deseja ver: "))
print()

num_antecessor = 0
num_atual = 0
ordem = 0

for i in range(0, num_escolhido):
    num_atual = num_antecessor + num_atual
    num_antecessor = num_atual - num_antecessor
    ordem = ordem + 1
    if(num_atual == 0):
        num_atual = num_atual + 1
    print(f"{ordem}° número: {num_atual}")

print(f"\nO {num_escolhido}° número é o {num_atual}")
    
    