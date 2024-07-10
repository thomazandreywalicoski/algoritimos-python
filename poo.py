class cachorro:

    def __init__(self, raca, cor, nome, sexo, peso, altura, data_nascimento, quantidade_comida_porcao):
        self.raca = raca
        self.cor = cor
        self.nome = nome
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.data_nascimento = data_nascimento
        self.quantidade_comida_porcao = quantidade_comida_porcao
        self.comida = 1000

    def comer(self):
        self.comida -= self.quantidade_comida_porcao
        print(f"O cachorro {self.nome} ainda possui {self.comida} gramas de comida")

    def latir(self):
        print(f"O cachorro {self.nome} está latindo!")

    def informacoes_cachorro(self):
        print("\nINFORMAÇÕES DO CACHORRO\n")
        print(f"RAÇA: {self.raca}")
        print(f"COR: {self.cor}")
        print(f"NOME: {self.nome}")
        print(f"SEXO: {self.sexo}")
        print(f"PESO: {self.peso} Kg")
        print(f"ALTURA: {self.altura} cm")
        print(f"DATA DE NASCIMENTO: {self.data_nascimento}")
        print(f"QUANTIDADE DE COMIDA: {self.quantidade_comida_porcao} gramas por refeição")

if __name__ == '__main__':
    meu_primeiro_cachorro = cachorro("Pitbull", "Marrom", "Maile", "Masculino", 5, 30.5, "10/10/2018", 80)
    print(meu_primeiro_cachorro.nome)

    segundo_cachorro = cachorro("Bulldog", "Caramelo", "Dog", "Masculino", 6, 30, "20/10/2016", 150)
    print(segundo_cachorro.cor)

    meu_primeiro_cachorro.latir()
    segundo_cachorro.latir()
    meu_primeiro_cachorro.comer()
    segundo_cachorro.comer()

    meu_primeiro_cachorro.informacoes_cachorro()
    segundo_cachorro.informacoes_cachorro()
