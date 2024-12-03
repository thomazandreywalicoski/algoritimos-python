from produto import Produto, produtos
from usuario import Usuario, usuarios
from carrinho import Carrinho, produto_adicionado_carrinho

import os
import time

class Loja:
    def __init__(self):
        self.opcao_selecionada = 0

    def menu_inicial(self):
        self.limpar()
        self.opcao_selecionada = 0

        while self.opcao_selecionada != 4:
            print("*" * 100)
            print(" " * 38, "------------------")
            print(" " * 38, "| LOJA DO THOMAZ |")
            print(" " * 38, "------------------")
            print("")
            print(" " * 12, "[ 1 ] ACESSAR LOJA    [ 2 ] CRIAR CONTA    [ 3 ] FAZER LOGIN    [ 4 ] SAIR")
            print("")
            print("*" * 100)

            self.opcao_selecionada = int(input("\nSELECIONE A OPÇÃO DESEJADA: "))

            while self.opcao_selecionada < 1 or self.opcao_selecionada > 4:
                self.opcao_selecionada = int(input("\nOPÇÃO INVÁLIDA! SELECIONE UMA OPÇÃO VÁLIDA: "))

            self.opcao_inicio(self.opcao_selecionada)

    def opcao_inicio(self, num_escolhido_inicio):
        match num_escolhido_inicio:
            case 1:
                self.acessar_loja()
            case 2:
                self.cadastrar_usuario()
            case 3:
                self.fazer_login()
            case 4:
                self.limpar()
                print("Saindo...")
                self.delay()
                exit()

    def acessar_loja(self):
        self.limpar()
        print(" " * 30, "=" * 33)
        print(" " * 30, "|              LOJA             |")
        print(" " * 30, "=" * 33, "\n")
        self.algum_produto_cadastrado = False

        for produto in produtos:
            produto.listarTodosProdutos()
            self.algum_produto_cadastrado = True

        if self.algum_produto_cadastrado:
            print("\n", " " * 10, "[ 1 ] ADICIONAR AO CARRINHO    [ 2 ] ACESSAR CARRINHO    [ 3 ] VOLTAR")

            self.escolha = int(input("\n>> "))

            while self.escolha < 1 or self.escolha > 3:
                print("OPÇÃO INVÁLIDA!")
                self.escolha = int(input("\n>> "))

            if self.escolha == 1:
                self.adicionar_carrinho()
            elif self.escolha == 2:
                self.carrinho()
            elif self.escolha == 3:
                self.menu_inicial()

        else:
            self.limpar()
            print("\n", " " * 23, "NENHUM PRODUTO DISPONÍVEL A VENDA NO MOMENTO!\n")
            self.delay()
            self.limpar()


    def carrinho(self):
        self.limpar()
        print(" " * 30, "=" * 33)
        print(" " * 30, "|            CARRINHO           |")
        print(" " * 30, "=" * 33, "\n")

        self.algum_produto_carrinho = False

        for produtos_carrinho in produto_adicionado_carrinho:
            produtos_carrinho.listar_produtos_carrinho()
            self.algum_produto_carrinho = True

        if self.algum_produto_carrinho:
            print("\n[ 1 ] VOLTAR")

            self.escolha = int(input("\n>> "))

            while self.escolha != 1:
                print("\nOPÇÃO INVÁLIDA! [ 1 ] VOLTAR")
                self.escolha = int(input("\n>> "))

            self.acessar_loja()

        else:
            self.limpar()
            print("\n", " " * 30, "NENHUM PRODUTO NO CARRINHO!")
            self.delay()
            self.limpar()

                
    def adicionar_carrinho(self):
        self.id_digitado = input("\nDIGITE O ID DO PRODUTO: ")

        self.produto_encontrado = False

        for produto_carrinho in produto_adicionado_carrinho:
            if self.id_digitado == str(produto_carrinho.get_id_produto()):
                self.limpar()
                print("\n", " " * 25, "ESSE PRODUTO JÁ ESTÁ NO CARRINHO")
                self.delay()
                self.limpar()
                self.acessar_loja()
                return

        for produto in produtos:
            if self.id_digitado == str(produto.get_id()):
                produto_carrinho = Carrinho(produto.get_id(), produto.get_nome(), produto.get_preco_venda())
                produto_adicionado_carrinho.append(produto_carrinho)
                self.limpar()
                print("\n", " " * 25, "PRODUTO ADICIONADO AO CARRINHO!")
                self.delay()
                self.limpar()
                self.produto_encontrado = True
                break

        if not self.produto_encontrado:
            self.limpar()
            print("\n", " " * 35, "NENHUM PRODUTO COM ESSE ID!")
            self.delay()
            self.limpar()

        self.acessar_loja()


    def cadastrar_usuario(self):
        cpf_cadastrado = False
        self.limpar()
        print(" " * 28, "=" * 39)
        print(" " * 28, "|          CADASTRAR USUÁRIO          |")
        print(" " * 28, "=" * 39, "\n")

        self.id_usuario = len(usuarios) + 1
        self.nome = str(input("NOME: "))
        self.cpf = str(input("CPF: "))

        cpf_cadastrado = True
        while cpf_cadastrado:
            cpf_cadastrado = False
            for usuario in usuarios:
                if self.cpf == str(usuario.get_cpf()):
                    cpf_cadastrado = True
                    print("\nJÁ EXISTE UM CADASTRO COM ESSE CPF!\n")
                    self.cpf = str(input("CPF: "))
                    break

        self.ano_nascimento = str(input("ANO DE NASCIMENTO: "))
        self.endereco = str(input("ENDEREÇO: "))
        print("\nAGORA DIGITE SEU NÍVEL DE ACESSO:\n")
        print("[ 1 ] ADMINISTRADOR    [ 2 ] USUÁRIO\n")
        self.nivel = int(input("NÍVEL DE ACESSO: "))
        self.email = str(input("E-MAIL: "))
        self.senha = str(input("SENHA: "))

        novo_usuario = Usuario(self.id_usuario, self.nome, self.cpf, self.ano_nascimento, self.endereco, self.nivel, self.email, self.senha)

        usuarios.append(novo_usuario)

        self.limpar()
        print("\n", " " * 30, "USUÁRIO CADASTRADO COM SUCESSO!\n")
        self.delay()
        self.limpar()
        self.menu_inicial()


    def fazer_login(self):
        self.limpar()
        print(" " * 30, "=" * 33)
        print(" " * 30, "|          FAZER LOGIN          |")
        print(" " * 30, "=" * 33, "\n")

        self.cpf_digitado = str(input("\nDIGITE SEU CPF: "))
        self.senha_digitada = str(input("DIGITE SUA SENHA: "))

        self.usuario_encontrado = False

        for usuario in usuarios:
            if self.cpf_digitado == usuario.get_cpf() and self.senha_digitada == usuario.get_senha():
                self.usuario_encontrado = True

                if usuario.get_nivel() == 1:
                    self.limpar()
                    print("\n", " " * 30, "LOGIN EFETUADO COM SUCESSO!\n")
                    self.delay()
                    self.limpar()
                    self.painel_controle()
                else:
                    self.limpar()
                    print("\n", " " * 20, "NEGADO! VOCÊ NÃO TEM PERMISSÃO COMO ADMINISTRADOR!\n")
                    self.delay()
                    self.limpar()
                break

        if not self.usuario_encontrado:
            self.limpar()
            print("\n", " " * 32, "CPF E/OU SENHA INCORRETOS!\n")
            self.delay()
            self.limpar()


    def painel_controle(self):
        self.limpar()
        print("*" * 100)
        print(" " * 36, "----------------------")
        print(" " * 36, "| PAINEL DE CONTROLE |")
        print(" " * 36, "----------------------")
        print("")
        print(" " * 12, "[ 1 ] CADASTRAR PRODUTO    [ 2 ] LISTAR PRODUTOS CADASTRADOS    [ 3 ] SAIR")
        print("")
        print("*" * 100)

        self.opcao_selecionada = int(input("\nSELECIONE A OPÇÃO DESEJADA: "))

        while self.opcao_selecionada < 1 or self.opcao_selecionada > 3:
            self.opcao_selecionada = int(input("\nOPÇÃO INVÁLIDA! SELECIONE UMA OPÇÃO VÁLIDA: "))

        if self.opcao_selecionada == 1:
            self.cadastrarProduto()
        elif self.opcao_selecionada == 2:
            self.listarProdutos()
        elif self.opcao_selecionada == 3:
            self.menu_inicial()

    def cadastrarProduto(self):
        self.limpar()
        print(" " * 28, "=" * 39)
        print(" " * 28, "|          CADASTRAR PRODUTO          |")
        print(" " * 28, "=" * 39, "\n")

        self.id = len(produtos) + 1
        self.nome = input("NOME: ")
        self.marca = input("MARCA: ")
        self.quantidade = int(input("QUANTIDADE: "))
        self.preco_venda = float(input("PREÇO VENDA: "))
        self.preco_fornecedor = float(input("PREÇO FORNECEDOR: "))
        self.estoque = int(input("ESTOQUE: "))
        self.descricao = input("DESCRIÇÃO: ")

        novo_produto = Produto(self.id, self.nome, self.marca, self.quantidade, self.preco_venda, self.preco_fornecedor, self.estoque, self.descricao)

        produtos.append(novo_produto)

        self.limpar()
        print("\n", " " * 30, "PRODUTO CADASTRADO COM SUCESSO!\n")
        self.delay()
        self.limpar()
        self.painel_controle()


    def listarProdutos(self):
        self.limpar()
        print(" " * 28, "=" * 42)
        print(" " * 28, "|          PRODUTOS CADASTRADOS          |")
        print(" " * 28, "=" * 42, "\n")

        self.algum_produto_cadastrado = False

        for produto in produtos:
            produto.listarTodosProdutos()
            self.algum_produto_cadastrado = True

        if self.algum_produto_cadastrado:
            print("\n", "*" * 100, "\n")
            print(" " * 16, "[ 1 ] VISUALIZAR    [ 2 ] EDITAR    [ 3 ] DELETAR   [ 4 ] VOLTAR\n")
            print("*" * 100)

            self.opcao = int(input("\nSELECIONE A OPÇÃO DESEJADA: "))

            while self.opcao < 1 or self.opcao > 4:
                self.opcao = int(input("OPÇÃO INVÁLIDA! SELECIONE UMA OPÇÃO VÁLIDA: "))

            if self.opcao == 1:
                self.visualizar_produto()
            elif self.opcao == 2:
                self.editar_produto()
            elif self.opcao == 3:
                self.deletar_produto()
            elif self.opcao == 4:
                self.painel_controle()
        else:
            self.limpar()
            print("\n", " " * 35, "NENHUM PRODUTO CADASTRADO!\n")
            self.delay()
            self.limpar()
            self.painel_controle()

    def visualizar_produto(self):
        self.limpar()
        print(" " * 26, "=" * 44)
        print(" " * 26,"|          INFORMAÇÕES DO PRODUTO          |")
        print(" " * 26,"=" * 44, "\n")

        self.id_produto = int(input("INFORME O ID DO PRODUTO QUE DESEJA VISUALIZAR: "))

        for produto in produtos:
            if produto.get_id() == self.id_produto:
                produto.visualizarProduto()
                break
        else:
            self.limpar()
            print("\n", " " * 26,"NENHUM PRODUTO ENCONTRADO COM ESSE ID!")
            self.delay()
            self.limpar()
            self.listarProdutos()

        print("\n[ 1 ] VOLTAR")
        self.opcao_voltar = int(input(">> "))

        while(self.opcao_voltar != 1):
            print("OPÇÃO INVÁLIDA! DIGITE [ 1 ] VOLTAR")
            self.opcao_voltar = int(input(">> "))

        self.listarProdutos()

    def editar_produto(self):
        self.limpar()
        print(" " * 28, "=" * 42)
        print(" " * 28, "|          EDITAR PRODUTO          |")
        print(" " * 28, "=" * 42, "\n")

        self.id_produto = int(input("INFORME O ID DO PRODUTO QUE DESEJA VISUALIZAR: "))

        self.produto_encontrado = False

        for produto in produtos:
            if produto.get_id() == self.id_produto:
                self.produto_encontrado = True

                print("\nDEIXE EM BRANCO PARA NÃO ALTERAR!\n")
                self.nome = str(input("NOME: ")) or produto.get_nome()
                self.marca = str(input("MARCA: ")) or produto.get_marca()
                self.quantidade = int(input("QUANTIDADE: ")) or produto.get_quantidade()
                self.preco_venda = float(input("PREÇO COMPRA: ")) or produto.get_preco_venda()
                self.preco_fornecedor = float(input("PREÇO FORNECEDOR: ")) or produto.get_preco_fornecedor()
                self.estoque = int(input("ESTOQUE: ")) or produto.get_estoque()
                self.descricao = str(input("DESCRIÇÃO: ")) or produto.get_descricao()

                produto.set_nome(self.nome)
                produto.set_marca(self.marca)
                produto.set_quantidade(self.quantidade)
                produto.set_preco_venda(self.preco_venda)
                produto.set_preco_fornecedor(self.preco_fornecedor)
                produto.set_estoque(self.estoque)
                produto.set_descricao(self.descricao)

                self.limpar()
                print("\n", " " * 32, "PRODUTO EDITADO COM SUCESSO!\n")
                self.delay()
                self.limpar()
                self.listarProdutos()
                return

        if not self.produto_encontrado:
            self.limpar()
            print("\n", " " * 32, "NENHUM PRODUTO ENCONTRADO COM ESSE ID!\n")
            self.delay()
            self.limpar()
            self.listarProdutos()

    def deletar_produto(self):
        self.limpar()
        print(" " * 28, "=" * 42)
        print(" " * 28, "|          DELETAR PRODUTO          |")
        print(" " * 28, "=" * 42, "\n")

        self.id_produto = int(input("INFORME O ID DO PRODUTO QUE DESEJA DELETAR: "))

        self.produto_encontrado = False

        for i, produto in enumerate(produtos):
            if produto.get_id() == self.id_produto:

                self.produto_encontrado = True

                del produtos[i]

                self.limpar()
                print("\n", " " * 32, "PRODUTO DELETADO COM SUCESSO!\n")
                self.delay()
                self.limpar()

                self.listarProdutos()
                return

        if not self.produto_encontrado:
            self.limpar()
            print("\n", " " * 32, "NENHUM PRODUTO ENCONTRADO COM ESSE ID!\n")
            self.delay()
            self.limpar()
            self.listarProdutos()

    def limpar(self):
        os.system('cls')

    def delay(self):
        time.sleep(3)
