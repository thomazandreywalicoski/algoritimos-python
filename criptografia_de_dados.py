from cryptography.fernet import Fernet

def criptografar_dados(dados, chave):
    cifra = Fernet(chave)
    dados_criptografados = cifra.encrypt(dados.encode())
    return dados_criptografados

def descriptografar_dados(dados_criptografados, chave):
    cifra = Fernet(chave)
    dados_descriptografados = cifra.decrypt(dados_criptografados).decode()
    return dados_descriptografados

# Chave de criptografia (gerada de forma segura em um caso real)
chave = Fernet.generate_key()

# Dado a ser criptografado
dados_para_criptografar = str(input("Digite para criptografar: "))

# Criptografar os dados
dados_criptografados = criptografar_dados(dados_para_criptografar, chave)
print("Dados criptografados:", dados_criptografados)

# Descriptografar os dados
dados_descriptografados = descriptografar_dados(dados_criptografados, chave)
print("Dados descriptografados:", dados_descriptografados)
