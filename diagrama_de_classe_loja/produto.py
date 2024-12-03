class Produto:

    def __init__(self, id, nome, marca, quantidade, preco_venda, preco_fornecedor, estoque, descricao):
        self._id = id
        self._nome = nome
        self._marca = marca
        self._quantidade = quantidade
        self._preco_venda = preco_venda
        self._preco_fornecedor = preco_fornecedor
        self._estoque = estoque
        self._descricao = descricao

    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome
    
    def get_marca(self):
        return self._marca
    
    def set_marca(self, marca):
        self._marca = marca
    
    def get_quantidade(self):
        return self._quantidade
    
    def set_quantidade(self, quantidade):
        self._quantidade = quantidade
    
    def get_preco_venda(self):
        return self._preco_venda
    
    def set_preco_venda(self, preco_venda):
        self._preco_venda = preco_venda
    
    def get_preco_fornecedor(self):
        return self._preco_fornecedor
    
    def set_preco_fornecedor(self, preco_fornecedor):
        self._preco_fornecedor = preco_fornecedor
    
    def get_estoque(self):
        return self._estoque
    
    def set_estoque(self, estoque):
        self._estoque = estoque
    
    def get_descricao(self):
        return self._descricao
    
    def set_descricao(self, descricao):
        self._descricao = descricao
    

    def listarTodosProdutos(self):
        print(f"\nID: {self.get_id()} \nNome do Produto: {self.get_nome()} \nPreço Venda: {self.get_preco_venda()}\n")
        print("-" * 50,)


    def visualizarProduto(self):
        print(f"\nID: {self._id} \nNome do Produto: {self._nome} \nMarca: {self._marca} \nQuantidade: {self._quantidade} \nPreço Venda: {self._preco_venda:.2f} \nPreço Fornecedor: {self._preco_fornecedor:.2f} \nEstoque: {self._estoque} \nDescrição: {self._descricao}")
        

    def editarProduto(self, nome, marca, quantidade, preco_venda, preco_fornecedor, estoque, descricao):
        self.set_nome(nome)
        self.set_marca(marca)
        self.set_quantidade(quantidade)
        self.set_preco_venda(preco_venda)
        self.set_preco_fornecedor(preco_fornecedor)
        self.set_estoque(estoque)
        self.set_descricao(descricao)

produtos = []