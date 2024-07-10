import os
import time
import random

pessoas = {}
verificar = {}
contador_cadastros = 0
situacao = False

# TÍTULO

def titulo():
    print("=" * 105)
    print(" " * 33, "PROJETO CAIXA ELETRÔNICO EM PYTHONaaa")
    print("=" * 105)

# MENU INICIAL

def menu_inicial():
    opcao_selecionada_inicio = 0

    titulo()

    while opcao_selecionada_inicio != 3:
        print("-" * 105)
        print(" " * 22, "[ 1 ] FAZER CADASTRO   [ 2 ] FAZER LOGIN    [ 3 ] SAIR")
        print("-" * 105)
        opcao_selecionada_inicio = int(input("\nSELECIONE A OPÇÃO DESEJADA: "))
        while opcao_selecionada_inicio < 1 or opcao_selecionada_inicio > 3:
            opcao_selecionada_inicio = int(input("\nOPÇÃO INVÁLIDA! SELECIONE UMA OPÇÃO VÁLIDA: "))
        opcao_inicio(opcao_selecionada_inicio)
        
    os.system("cls") or None
    print("=" * 105)
    print(" " * 42, "PROGRAMA FINALIZADO!")
    print("=" * 105)

# OPÇÃO MENU INICIAL

def opcao_inicio(num_escolhido_inicio):
    match num_escolhido_inicio:
        case 1:
            fazer_cadastro()
        case 2:
            fazer_login()

# MENU  

def menu():
    opcao_selecionada = 0

    titulo()

    print("-" * 105)
    print(" " * 20, "[ 1 ] SACAR    [ 2 ] DEPOSITAR    [ 3 ] EXTRATO    [ 4 ] SAIR")
    print("-" * 105)
    opcao_selecionada = int(input("\nSELECIONE A OPÇÃO DESEJADA: "))
    while opcao_selecionada < 1 or opcao_selecionada > 5:
        opcao_selecionada = int(input("\nOPÇÃO INVÁLIDA! SELECIONE UMA OPÇÃO VÁLIDA: "))
    opcao(opcao_selecionada)
    

# OPÇÃO MENU

def opcao(num_escolhido):
    match num_escolhido:
        case 1:
            sacar()
        case 2:
            depositar()
        case 3:
            extrato()
        case 4:
            menu_inicial()


# FAZER CADASTRO

def fazer_cadastro():
    global contador_cadastros
    situacao = False
    os.system("cls") or None
    print("=" * 105)
    print(" " * 44, "FAZER CADASTRO")
    print("=" * 105)
    
    nome = str(input("\nDIGITE SEU NOME: ")).capitalize()
    
    dados = {}
    
    dados["cpf"] = str(input("DIGITE SEU CPF: "))
    
    for pessoa,  valor in list(pessoas.items()):
        if valor["cpf"] == dados["cpf"]:
            situacao = True
    if situacao == True:
        os.system("cls") or None
        print("-" * 105)
        print(" " * 35, "JÁ EXISTE UM CADASTRO COM ESSE CPF!")
        print("-" * 105)
        time.sleep(2)
        os.system("cls") or None

    else:
        print("\nCRIE UMA SENHA (GUARDE ESSA SENHA, POIS VOCÊ IRA PRECISAR DELA POSTERIORMENTE)\n")
        dados["senha"] = str(input("SENHA: "))
        dados["saldo"] = 0
        dados["codigo_seguranca"] = random.randint(10000, 99999)
        dados["saques_realizados"] = 0
        dados["depositos_realizados"] = 0
        pessoas[f"{nome}"] = dados
    
        print("\nCADASTRANDO...")
        time.sleep(2)
        os.system("cls") or None
        print("-" * 105)
        print(" " * 35, "CADASTRO REALIZADO COM SUCESSO!")
        print("-" * 105)
        time.sleep(2)
        os.system("cls") or None
            
        contador_cadastros += 1

        titulo()
       

# FAZER LOGIN

def fazer_login():
    global cpf_login, senha_login
    if contador_cadastros < 1:
        os.system("cls") or None
        print("-" * 105)
        print(" " * 38, "NENHUM CADASTRO REALIZADO!")
        print("-" * 105)
        time.sleep(2)
        os.system("cls") or None
    else:
        situacao = False
        
        os.system("cls") or None
        print("=" * 105)
        print(" " * 48, "FAZER LOGIN")
        print("=" * 105)

        cpf_login = str(input("\nINSIRA SEU CPF: "))
        senha_login = str(input("INSIRA SUA SENHA: "))

        for valor, login in pessoas.items():
                 
            if login["cpf"] == cpf_login and login["senha"] == senha_login:
                situacao = True
                os.system("cls") or None
                print("-" * 105)
                print(" " * 38, "LOGIN EFETUADO COM SUCESSO!")
                print("-" * 105)
                time.sleep(2)
                os.system("cls") or None

                verifica = {}

                verifica["cpf_verifica"] = cpf_login
                verifica["senha_verifica"] = senha_login
                verificar["verificacao_login"] = verifica 

                menu()
                       
        if not situacao:
            os.system("cls") or None
            print("-" * 105)
            print(" " * 38, "NOME E/OU SENHAS INVÁLIDOS!")
            print("-" * 105)
            time.sleep(2)
            os.system("cls") or None 

    titulo()
    

# SACAR

def sacar():
    global cpf_login, senha_login

    situacao = False

    os.system("cls") or None
    print("=" * 105)
    print(" " * 50, "SACAR")
    print("=" * 105)
                 
    print("\nVERIFICAÇÃO DE SEGURANÇA PARA SACAR!")
    print("-" * 40)

    cpf_digitado = str(input("\nDIGITE SEU CPF PARA CONTINUAR: "))
    senha_digitada = str(input("DIGITE SUA SENHA PARA CONTINUAR: "))

    for verifica, codigo in pessoas.items():
        if cpf_digitado == codigo["cpf"] and senha_digitada == codigo["senha"]:         
            
            print("\nCÓDIGO DE SEGURANÇA (GERADO AUTOMATICAMENTE PELO SISTEMA)\n")
            print("CÓDIGO:", codigo["codigo_seguranca"])
            codigo_seguranca_digitado = int(input("\nDIGITE O CÓDIGO DE SEGURANÇA ACIMA: "))    
    
    for value, verifica_login in verificar.items():
        
        if cpf_digitado == verifica_login["cpf_verifica"] and senha_digitada == verifica_login["senha_verifica"]:
            
            for valor, nome_saque in pessoas.items():

                if cpf_login == nome_saque["cpf"] and senha_login == nome_saque["senha"] and codigo_seguranca_digitado == nome_saque["codigo_seguranca"]:
                
                    situacao = True
                        
                    os.system("cls") or None
                    print("-" * 105)
                    print(" " * 39, "VERIFICAÇÃO CONCLUÍDA!")
                    print("-" * 105)
                    time.sleep(2)
                    os.system("cls") or None 
                        
                    print("INFORMAÇÕES PESSOAIS:")
                    print("-" * 20)
                    print("NOME:", valor)
                    print("SALDO: R$", nome_saque["saldo"])
                    print("-" * 20)
                                                                                
                    saque = float(input("\nDIGITE O VALOR QUE DESEJA SACAR: R$"))

                    if saque > nome_saque["saldo"]:
                        os.system("cls") or None
                        print("-" * 105)
                        print(" " * 23, "NÃO É POSSÍVEL REALIZAR UM SAQUE POIS SEU SALDO É DE R$", nome_saque["saldo"])
                        print("-" * 105)
                        time.sleep(3)
                        os.system("cls") or None
                        
                    elif saque < 1:
                        os.system("cls") or None
                        print("-" * 105)
                        print(" " * 28, "NEGADO! O VALOR MINÍMO PARA SACAR E DE R$1,00!")
                        print("-" * 105)
                        time.sleep(3)
                        os.system("cls") or None
                    
                    else:                   
                        valor_restante = nome_saque["saldo"] - saque
                                            
                        nome_saque["saldo"] = valor_restante
                                                
                        print("\nCONTANDO CÉDULAS...")
                        time.sleep(2)
                                    
                        os.system("cls") or None
                        print("-" * 105)
                        print(" " * 39, "SAQUE REALIZADO COM SUCESSO!")
                        print("-" * 105)
                        time.sleep(2)
                        os.system("cls") or None  

                        cpf_digitado = ""
                        senha_digitada = ""
                            
                        nome_saque["saques_realizados"] += 1
                        
                    break
                          
    if not situacao:
        os.system("cls") or None
        print("-" * 105)
        print(" " * 27, "CPF E/OU SENHA E/OU CÓDIGO DE SEGURANÇA INVÁLIDOS!")
        print("-" * 105)
        time.sleep(3)
        os.system("cls") or None
              
    menu()
        
                  
# DEPOSITAR 

def depositar():
    global cpf_login, senha_login
    
    situacao = False

    os.system("cls") or None
    print("=" * 105)
    print(" " * 47, "DEPOSITAR")
    print("=" * 105)
                    
    print("\nVERIFICAÇÃO DE SEGURANÇA PARA DEPOSITAR!")
    print("-" * 44)

    cpf_digitado = str(input("\nDIGITE SEU CPF PARA CONTINUAR: "))
    senha_digitada = str(input("DIGITE SUA SENHA PARA CONTINUAR: "))

    for verifica, codigo in pessoas.items():
        if cpf_digitado == codigo["cpf"] and senha_digitada == codigo["senha"]:         
            
            print("\nCÓDIGO DE SEGURANÇA (GERADO AUTOMATICAMENTE PELO SISTEMA)\n")
            print("CÓDIGO:", codigo["codigo_seguranca"])
            codigo_seguranca_digitado = int(input("\nDIGITE O CÓDIGO DE SEGURANÇA ACIMA: "))    
    
    for value, verifica_login in verificar.items():
        
        if cpf_digitado == verifica_login["cpf_verifica"] and senha_digitada == verifica_login["senha_verifica"]:
            
            for valor, nome_deposito in pessoas.items():

                if cpf_login == nome_deposito["cpf"] and senha_login == nome_deposito["senha"] and codigo_seguranca_digitado == nome_deposito["codigo_seguranca"]:
                
                    situacao = True
                        
                    os.system("cls") or None
                    print("-" * 105)
                    print(" " * 39, "VERIFICAÇÃO CONCLUÍDA!")
                    print("-" * 105)
                    time.sleep(2)
                    os.system("cls") or None 
                        
                    print("INFORMAÇÕES PESSOAIS:")
                    print("-" * 20)
                    print("NOME:", valor)
                    print("SALDO: R$", nome_deposito["saldo"])
                    print("-" * 20)

                    deposito = float(input("\nDIGITE O VALOR QUE DESEJA DEPOSITAR: "))
         
                    if deposito < 1:
                        os.system("cls") or None
                        print("-" * 105)
                        print(" " * 26, "NEGADO! NÃO É POSSÍVEL DEPOSITAR UM VALOR MENOR QUE R$1,00!")
                        print("-" * 105)
                        time.sleep(2)
                        os.system("cls") or None
                    else:
                                        
                        valor_restante = nome_deposito["saldo"] + deposito
                                        
                        nome_deposito["saldo"] = valor_restante
                                            
                        print("\nDEPOSITANDO DINHEIRO...")
                        time.sleep(2)
                                
                        os.system("cls") or None
                        print("-" * 105)
                        print(" " * 36, "DEPOSITO REALIZADO COM SUCESSO!")
                        print("-" * 105)
                        time.sleep(2)
                        os.system("cls") or None  

                        cpf_digitado = ""
                        senha_digitada = ""
                        
                        nome_deposito["depositos_realizados"] += 1

                    break
                          
    if not situacao:
        print()
        os.system("cls") or None
        print("-" * 105)
        print(" " * 27, "CPF E/OU SENHA E/OU CÓDIGO DE SEGURANÇA INVÁLIDOS!")
        print("-" * 105)
        time.sleep(3)
        os.system("cls") or None
              
    menu()
                                                                                
    
# EXTRATO

def extrato():     
    situacao = False

    print("\nCARREGANDO EXTRATO...")
    time.sleep(2)
    
    os.system("cls") or None
    print("=" * 105)
    print(" " * 47, "EXTRATO")
    print("=" * 105)

    print("\nVERIFICAÇÃO DE SEGURANÇA PARA VER O EXTRATO!\n")
    cpf_extrato = str(input("DIGITE SEU CPF PARA CONTINUAR: "))
    senha_extrato = str(input("DIGITE SUA SENHA PARA CONTINUAR: "))  
   
    for value, verifica_extrato in verificar.items():
        
        if cpf_extrato == verifica_extrato["cpf_verifica"] and senha_extrato == verifica_extrato["senha_verifica"]:
            
            for informacoes, informacao in pessoas.items():

                if cpf_login == informacao["cpf"] and senha_login == informacao["senha"]:
                
                    situacao = True  

                    os.system("cls") or None
                    print("-" * 105)
                    print(" " * 39, "VERIFICAÇÃO CONCLUÍDA!")
                    print("-" * 105)
                    time.sleep(2)
                    os.system("cls") or None 

                    print("INFORMAÇÕES PESSOAIS:")
                    print("-" * 30)
                    print("NOME:", informacoes)
                    print("CPF:", informacao["cpf"])
                    print("SALDO: R$", informacao["saldo"])
                    print("SAQUES REALIZADOS:", informacao["saques_realizados"])
                    print("DEPOSITOS REALIZADOS:", informacao["depositos_realizados"])
                    print("-" * 30)
                    
                    break

                else:
                    situacao = False
    if situacao == False:  
        os.system("cls") or None
        print("-" * 105)
        print(" " * 40, "CPF E/OU SENHA INVÁLIDOS!")
        print("-" * 105)
        time.sleep(3)
        os.system("cls") or None

    menu()
            

menu_inicial()