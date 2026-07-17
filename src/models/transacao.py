class Transacao:
    def __init__(self, id: int, tipo: str, valor: float, conta_id: int):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.conta_id = conta_id
