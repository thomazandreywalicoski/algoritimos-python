print("TABUADA EM PYTHON")
print("-" * 50)

num = int(input("\nDigite o número da Tabuada que deseja: "))

for c in range(1,11):
    print(f"{c} x {num} = {c * num}")