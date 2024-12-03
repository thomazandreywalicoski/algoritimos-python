class Veiculo:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

    def som(self):
        print(f"{self.nome} da marca {self.marca} faz um som.")

    def pode_transportar_pessoas(self):
        print("Esse veículo pode transportar pessoas.")

    def pode_ligar(self):
        print("Esse veículo pode ligar.")

class Empinar:
    def pode_empinar(self):
        print("Esse veículo pode empinar.")

class Voar:
    def pode_voar(self):
        print("Esse veículo pode voar.")
    
class Buzinar:
    def pode_buzinar(self):
        print("Esse veículo pode buzinar.")

class Estepe:
    def tem_estepe(self):
        print("Esse veículo tem estepe.")


class Carro(Veiculo, Buzinar, Estepe):
    def __init__(self, nome, marca):
        Veiculo.__init__(self, nome, marca)

class Aviao(Veiculo, Voar):
    def __init__(self, nome, marca):
        Veiculo.__init__(self, nome, marca)

class Moto(Veiculo, Empinar, Buzinar):
    def __init__(self, nome, marca):
        Veiculo.__init__(self, nome, marca)

class Transforms(Veiculo, Empinar, Voar, Estepe):
    def __init__(self, nome, marca):
        Veiculo.__init__(self, nome, marca)

if __name__ == "__main__":
    carro = Carro("Fox", "Volkswagen")
    carro.som()
    carro.pode_transportar_pessoas()
    carro.pode_buzinar()
    carro.pode_ligar()
    carro.tem_estepe()

    aviao = Aviao("Boeing 747", "Boeing")
    aviao.som()
    aviao.pode_voar()
    aviao.pode_transportar_pessoas()
    aviao.pode_ligar()

    moto = Moto("Lander", "Yamaha")
    moto.som()
    moto.pode_empinar()
    moto.pode_transportar_pessoas()
    moto.pode_buzinar()
    moto.pode_ligar()

    transforms = Transforms("Optimus Prime", "Cybertron")
    transforms.som()
    transforms.pode_voar()
    transforms.pode_empinar()
    transforms.pode_transportar_pessoas()
    transforms.pode_ligar()
    transforms.tem_estepe()
