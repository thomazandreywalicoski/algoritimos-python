class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        print(f"{self.nome} faz um som.")

class Mamifero(Animal):
    def __init__(self, nome, tipo_de_pelo):
        super().__init__(nome)
        self.tipo_de_pelo = tipo_de_pelo

    def amamentar(self):
        print(f"{self.nome} está amentando seus filhotes.")

class Cachorro(Mamifero):
    def __init__(self, nome, tipo_de_pelo, raça):
        super().__init__(nome, tipo_de_pelo)
        self.raça = raça

    def latir(self):
        print(f"{self.nome} está latindo.")

if __name__ == "__main__":
    cachorro = Cachorro("Maile", "Curto", "Labrador")
    cachorro.falar()
    cachorro.amamentar()
    cachorro.latir()