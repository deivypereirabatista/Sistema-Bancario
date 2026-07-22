from models.conta import Conta
from models.cliente import Cliente
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

    def find_by_cliente(cliente: Cliente):
        conta_cliente = []
        for conta in contas:
            if conta.cliente == cliente:
                conta_cliente.append(conta)
        return conta_cliente

    def delete(numero:str):
        for index, conta in enumerate(contas):
            if conta.numero == numero:
                contas.pop(index)
