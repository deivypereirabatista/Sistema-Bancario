from models.cliente import Cliente

class Conta:
    def __init__(self, numero: str, agencia:str, cliente: Cliente):
        
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente

    def __str__(self):
        return (
            "=================================\n"
            f"Numero da Conta: {self.numero}\n" 
            f"Agência: {self.agencia}\n" 
            "================================="
        )