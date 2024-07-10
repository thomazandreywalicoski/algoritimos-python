idade = int(input("Digite sua idade: "))

if idade >= 18 and idade <= 70:
    situacao = "OBRIGATÓRIO!"
elif idade < 16:
    situacao = "PROIBIDO!"
else:
    situacao = "FACULTATIVO!"

print(f"Você tem {idade} anos e seu voto é {situacao}")