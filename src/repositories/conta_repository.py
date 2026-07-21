from models.conta import Conta
from database.banco import contas

class ContaRepository:

    def create(conta: Conta):
        contas.append(conta)

    def find_all():
        return contas

    def find_by_numero(numero: str):
        for conta in contas:
            if conta.numero == numero:
                return conta
            
        return None

    def delete(numero:str):
        for index, conta in enumerate(contas):
            if conta.numero == numero:
                contas.pop(index)
