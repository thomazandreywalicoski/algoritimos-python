class Carrinho:

    def __init__(self, id_produto, nome, preco):
        self._id_produto = id_produto
        self._nome = nome
        self._preco = preco

    def get_id_produto(self):
        return self._id_produto
    
    def set_id_produto(self, id_produto):
        self._id_produto = id_produto
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome
    
    def get_preco(self):
        return self._preco
    
    def set_preco(self, preco):
        self._preco = preco

    
    def listar_produtos_carrinho(self):
        print(f"ID: {self._id_produto}, Produto: {self._nome}, Preço: {self._preco}")


produto_adicionado_carrinho = []
