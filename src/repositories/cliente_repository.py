from models.cliente import Cliente
from database.banco import clientes

class ClienteRepository:

    def create(cliente: Cliente):
        clientes.append(cliente)

    def find_all():
        return clientes

    def find_by_nome(nome: str):
        for cliente in clientes:
            if cliente.nome == nome:
                return cliente

        return None

    def update(novo_cliente: Cliente, nome:str):
        for index, cliente in enumerate(clientes):
            if cliente.nome == nome:
                clientes[index] = novo_cliente

        return None

    def delete(nome:str):
        for index, cliente in enumerate(clientes):
            if cliente.nome == nome:
                clientes.pop(index)