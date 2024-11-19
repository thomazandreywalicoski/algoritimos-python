class Animal:
    def __init__(self, nome):
        self.nome = nome

    def pode_falar(self):
        print(f"{self.nome} faz um som.")

class Voar:
    def pode_voar(self):
        print("Esse animal pode voar.")

class Botar:
    def pode_botar(self):
        print("Esse animal pode botar.")

class Nadar:
    def pode_nadar(self):
        print("Esse animal pode nadar.")

class Pato(Animal, Voar, Botar, Nadar):
    def __init__(self, nome):
        Animal.__init__(self, nome) # Inicializa a clase base Animal

class Galinha(Animal, Botar):
    def __init__(self, nome):
        Animal.__init__(self, nome) # Inicializa a clase base Animal

class Ornitorinco(Animal, Voar, Botar, Nadar):
    def __init__(self, nome):
        Animal.__init__(self, nome) # Inicializa a clase base Animal

if __name__ == "__main__":
    pato = Pato("Donalt")
    pato.pode_falar()
    pato.pode_voar()
    pato.pode_nadar()
    pato.pode_botar()

    galinha = Galinha("Pepi")
    galinha.pode_falar()
    galinha.pode_botar()

    ornitorinco = Ornitorinco("Blue")
    ornitorinco.pode_falar()
    ornitorinco.pode_botar()
    ornitorinco.pode_nadar()