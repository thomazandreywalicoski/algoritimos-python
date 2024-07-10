contador_saque = 0
contador_deposito = 0

def titulo():
    print("=" * 105)
    print(" " * 32, "PROJETO CAIXA ELETRÔNICO EM PYTHON")
    print("=" * 105)

titulo()

def valorInicial():
    global nome, saldo
    nome = str(input("\nDIGITE SEU NOME: "))
    saldo = float(input("DIGITE O VALOR QUE DESEJA TER NA CONTA: R$"))
    print("\n")
    
valorInicial()

def sacar():
    global contador_saque
    global saldo
    print("=" * 105)
    print(" " * 45, "[ 2 ] SACAR")
    print("=" * 105)
    print("\nINFORMAÇÕES DISPONÍVEIS:\n")
    print("-" * 20)
    print(f"NOME: {nome}")
    print(f"SALDO: {saldo}")
   
    saque = float(input("\nDIGITE O VALOR QUE DESEJA SACAR: "))

    valor_restante = saldo - saque
    
    if saque > saldo:
        print("\nNEGADO! SEU SALDO DISPONÍVEL É R$", saldo)
        print("\n")
    else:
        saldo = valor_restante
        print("\nSAQUE REALIZADO COM SUCESSO!")
    contador_saque += 1

def depositar():
    global contador_deposito
    global saldo
    print("=" * 105)
    print(" " * 42, "[ 3 ] DEPOSITAR")
    print("=" * 105)
    print("\nINFORMAÇÕES DISPONÍVEIS:\n")
    print("-" * 20)
    print("NOME:", nome)
    print("SALDO:", saldo)
    print("-" * 20)

    deposito = float(input("\nDIGITE O VALOR QUE DESEJA DEPOSITAR: "))

    valor_depositado = saldo + deposito
    
    if deposito < 0:
        print("\nNÃO TEM COMO ADICIONAR UM VALOR NEGATIVO!")
    else:
        saldo = valor_depositado
        print("\nDEPOSITO REALIZADO COM SUCESSO!")
    contador_deposito += 1

def extrato():
    print("\nINFORMAÇÕES DISPONÍVEIS:\n")
    print("-" * 30)
    print("NOME:", nome)
    print("SALDO:", saldo)
    print("SAQUES REALIZADOS:", contador_saque)
    print("DEPOSITOS REALIZADOS", contador_deposito)
    print("-" * 30)

def menu():
    opcao_selecionada = 0
    while opcao_selecionada != 4:
        print("-" * 105)
        print(" " * 18, "[ 1 ] EXTRATO    [ 2 ] SACAR    [ 3 ] DEPOSITAR    [ 4 ] SAIR")
        print("-" * 105)
        opcao_selecionada = int(input("\nSELECIONE A OPÇÃO DESEJADA: "))
        while opcao_selecionada < 1 or opcao_selecionada > 4:
            opcao_selecionada = int(input("\nOPÇÃO INVÁLIDA! SELECIONE UMA OPÇÃO VÁLIDA: "))
        opcao(opcao_selecionada)
    print("=" * 105)
    print(" " * 40, "PROGRAMA FINALIZADO")
    print("=" * 105)

def opcao(num_escolhido):
    match(num_escolhido):
        case 1:
            extrato()
        case 2:
            sacar()
        case 3:
            depositar()

menu()