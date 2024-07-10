import os
import time

pacientes = []
situacao = False

contador_cadastro = 1

# TÍTULO

def titulo():
    print("=" * 105)
    print(" " * 35, "PROJETO VACINAÇÃO EM PYTHON")
    print("=" * 105)

titulo()

# MENU

def menu():
    opcao_selecionada = 0
    while opcao_selecionada != 5:
        print("-" * 105)
        print("1) CADASTRAR VACINA\t2) LISTAR CADASTROS\t3) CONSULTAR POR CPF\t4) EXCLUIR CADASTRO\t5) SAIR")
        print("-" * 105)
        opcao_selecionada = int(input("\nSELECIONE A OPÇÃO DESEJADA: "))
        while opcao_selecionada < 1 or opcao_selecionada > 5:
            opcao_selecionada = int(input("\nOPÇÃO INVÁLIDA! SELECIONE UMA OPÇÃO VÁLIDA: "))
        opcao(opcao_selecionada)
    print("\nPROGRAMA FINALIZADO")

# CADASTRAR

def cadastrar_vacina():
    situacao = False
    if contador_cadastro < 50:
        print("=" * 105)
        print(" " * 35, "1) CADASTRAR PACIENTE")
        print("=" * 105)
        print("\nINFORME TODOS OS DADOS A SEGUIR:\n")
        
        dados_paciente = {}

        dados_paciente["nome_paciente"] = str(input("\nNOME DO PACIENTE: "))
        dados_paciente["cpf_paciente"] = int(input("CPF DO PACIENTE: "))
        for paciente in pacientes:
            if paciente["cpf_paciente"] == dados_paciente["cpf_paciente"]:
                situacao = True
        if situacao == True:
            os.system("cls") or None
            print("-" * 105)
            print(" " * 35, "JÁ EXISTE UM CADASTRO COM ESSE CPF!")
            print("-" * 105)
            time.sleep(2)
            os.system("cls") or None

        else:
            dados_paciente["vacina_aplicada"] = str(input("VACINA APICADA: "))
            dados_paciente["data_aplicacao"] = str(input("DATA DA APLICAÇÃO: "))
            pacientes.append(dados_paciente)

            print("\nPACIENTE CADASTRADO COM SUCESSO!\n")

# LISTAR APLICAÇÕES

def listar_aplicacoes():
    print("TODOS OS CADASTROS")

    for cadastro in pacientes:
        print("\nDADOS DO PACIENTE:")
        print("-" * 30)
        print("NOME DO PACIENTE:", cadastro["nome_paciente"])
        print("CPF DO PACIENTE:", cadastro["cpf_paciente"])
        print("VACINA APLICADA:", cadastro["vacina_aplicada"])
        print("DATA DA APLICAÇÃO:", cadastro["data_aplicacao"])
       
# CONSULTAR POR CPF

def consultar_por_cpf():
    print("CONSULTAR POR CPF")

    cpf_digitado = int(input("DIGITE O CPF PARA BUSCAR: "))

    for paciente in pacientes: 
        if cpf_digitado == paciente["cpf_paciente"]:
            print("DADOS DO PACIENTE:\n")
            print("NOME DO PACIENTE:", paciente["nome_paciente"])
            print("CPF DO PACIENTE:", paciente["cpf_paciente"])
            print("VACINA APLICADA:", paciente["vacina_aplicada"])
            print("DATA DA APLICAÇÃO:", paciente["data_aplicacao"])

def excluir_cadastro():
    print("EXCLUIR CADASTRO")

    cpf_excluir = int(input("DIGITE O CPF DO CADASTRO QUE DESEJA EXCLUIR: "))

    for cadastro in pacientes:
        if cpf_excluir == cadastro["cpf_paciente"]:
            pacientes.remove(cadastro)
        

def opcao(num_escolhido):
    match(num_escolhido):
        case 1:
            cadastrar_vacina()
        case 2:
            listar_aplicacoes()
        case 3:
            consultar_por_cpf()
        case 4:
            excluir_cadastro()
menu()


