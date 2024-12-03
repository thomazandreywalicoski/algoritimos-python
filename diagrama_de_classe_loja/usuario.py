class Usuario:

    def __init__(self, id_usuario, nome, cpf, ano_nascimento, endereco, nivel, email, senha):
        self._id_usuario = id_usuario
        self._nome = nome
        self._cpf = cpf
        self._ano_nascimento = ano_nascimento
        self._endereco = endereco
        self._nivel = nivel
        self._email = email
        self._senha = senha

    def get_id_usuario(self):
        return self._id_usuario
    
    def set_id_usuario(self, id_usuario):
        self._id_usuario = id_usuario
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome
    
    def get_cpf(self):
        return self._cpf
    
    def set_cpf(self, cpf):
        self._cpf = cpf
    
    def get_ano_nascimento(self):
        return self._ano_nascimento
    
    def set_ano_nascimento(self, ano_nascimento):
        self._ano_nascimento = ano_nascimento
    
    def get_endereco(self):
        return self._endereco
    
    def set_endereco(self, endereco):
        self._endereco = endereco
    
    def get_nivel(self):
        return self._nivel
    
    def set_nivel(self, nivel):
        self._nivel = nivel
    
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email
    
    def get_senha(self):
        return self._senha
    
    def set_senha(self, senha):
        self._senha = senha

usuarios = []