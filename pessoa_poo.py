class Pessoa:
    def __init__(self, nome, sexo, cpf, ano_nascimento, salario_bruto):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ano_nascimento = ano_nascimento
        self.idade = self.calcular_idade()
        self.salario_bruto = salario_bruto
        self.inss = self.calcular_desconto_inss()
        self.irrf = self.calcular_desconto_irrf()
        self.salario_liquido = self.calcular_salario_liquido()

# CALCULAR IDADE

    def calcular_idade(self):
        return 2024 - self.ano_nascimento
    
# CALCULAR INSS
    
    def calcular_inss(self):
        salario = self.salario_bruto

        if salario <= 1412.00:
            return self.calcular_porcentagem(7.5)
        elif salario > 1412.00 and salario <= 2666.68:
            return self.calcular_porcentagem(9.00)
        elif salario > 2666.68 and salario <= 4000.03:
            return self.calcular_porcentagem(12.00)
        else:
            return self.calcular_porcentagem(14.00)
        
# CALCULAR IRRF
    
    def calcular_irrf(self):
        salario = self.salario_bruto

        if salario > 2259.20 and salario <= 2826.65:
            return self.calcular_porcentagem(7.5)
        elif salario > 2826.65 and salario <= 3751.05:
            return self.calcular_porcentagem(15.00)
        elif salario > 3751.05 and salario <= 4664.68:
            return self.calcular_porcentagem(22.50)
        elif salario > 4664.68:
            return self.calcular_porcentagem(27.50)
        else:
            return 0.0
        
# CALCULAR PORCENTAGEM

    def calcular_porcentagem(self, porcentagem):
        return (self.salario_bruto * porcentagem) / 100
    
# CALCULAR DESCONTO INSS

    def calcular_desconto_inss(self):
        return (self.salario_bruto + self.calcular_inss()) - self.salario_bruto
    
# CALCULAR DESCONTO IRRF

    def calcular_desconto_irrf(self):
        return (self.salario_bruto + self.calcular_irrf()) - self.salario_bruto
           

# CALCULAR SALÁRIO LIQUÍDO
    
    def calcular_salario_liquido(self):
        descontos = self.calcular_inss() + self.calcular_irrf()
        return self.salario_bruto - descontos
    
# IMPRIMIR DADOS

    def imprimir_dados(self):
        print("\nINFORMAÇÕES DA PESSOA\n")
        print(f"NOME: {self.nome}")
        print(f"SEXO: {self.sexo}")
        print(f"CPF: {self.cpf}")
        print(f"ANO DE NASCIMENTO: {self.ano_nascimento}")
        print(f"IDADE: {self.idade}")
        print(f"SALÁRIO BRUTO: {self.salario_bruto}")
        print(f"INSS: {self.inss}")
        print(f"IRRF: {self.irrf}")
        print(f"SALÁRIO LIQUÍDO: {self.salario_liquido}")
        print("-" * 50)

if __name__ == '__main__':
    primeira_pessoa = Pessoa("Thomaz", "Masculino", 12312312312, 2004, 5000)
    primeira_pessoa.imprimir_dados()
    segunda_pessoa = Pessoa("Aldimara", "Feminino", 10101010101, 1975, 4000)
    segunda_pessoa.imprimir_dados()
    terceira_pessoa = Pessoa("Cassiano", "Masculino", 10987654321, 2004, 6000)
    terceira_pessoa.imprimir_dados()
    quarta_pessoa = Pessoa("Osmar", "Masculino", 12345678910, 1966, 7000)
    quarta_pessoa.imprimir_dados()

    quinta_pessoa = Pessoa("", "", "", 0, 0)
    quinta_pessoa.nome = input("\nDigite seu nome: ")
    quinta_pessoa.sexo = input("Digite seu sexo: ")
    quinta_pessoa.cpf = input("Digite seu CPF: ")
    quinta_pessoa.ano_nascimento = int(input("Digite seu Ano de Nascimento: "))
    quinta_pessoa.salario_bruto = float(input("Digite seu Salário Bruto: "))
    quinta_pessoa.idade = quinta_pessoa.calcular_idade()
    quinta_pessoa.inss = quinta_pessoa.calcular_desconto_inss()
    quinta_pessoa.irrf = quinta_pessoa.calcular_desconto_irrf()
    quinta_pessoa.salario_liquido = quinta_pessoa.calcular_salario_liquido()
    quinta_pessoa.imprimir_dados()