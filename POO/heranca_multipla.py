class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} faz um som.")

class Voar:
    def pode_voar(self):
        print("Esse animal pode voar.")

class Pato(Animal, Voar):
    def __init__(self, nome):
        Animal.__init__(self, nome) # Inicializa a clase base Animal

    def nadar(self):
        print(f"{self.nome} está nadando!")

if __name__ == "__main__":
    pato = Pato("Donalt")
    pato.falar()
    pato.pode_voar()
    pato.nadar()