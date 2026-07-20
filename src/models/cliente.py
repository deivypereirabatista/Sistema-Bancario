class Cliente:
    def __init__(self, nome: str, cpf: str, data_nascimento:str, endereco:str):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def __str__(self):
        return (
            "=================================\n"
            f"Nome: {self.nome}\n" 
            f"CPF: {self.cpf}\n" 
            f"Data de Nascimento: {self.data_nascimento}\n" 
            f"Endereço: {self.endereco}\n"
            "================================="
        )

