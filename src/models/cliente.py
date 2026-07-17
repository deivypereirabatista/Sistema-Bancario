class Cliente:
    def __init__(self, nome: str, cpf: str, data_nascimento:str, endereco:str):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

        self.contas = []

