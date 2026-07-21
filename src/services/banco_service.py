from repositories.cliente_repository import ClienteRepository
from repositories.conta_repository import ContaRepository
from models.cliente import Cliente
from models.conta import Conta

class ClinteService:

    def create(cliente: Cliente):
        ClienteRepository.create(cliente)

    def find_all(): 
        return ClienteRepository.find_all()
        
    def find_by_nome(nome:str):
        return ClienteRepository.find_by_nome(nome)

    def update(novo_cliente: Cliente, nome: str):
        ClienteRepository.update(nome, novo_cliente)

    def delete(nome: str):
        ClienteRepository.delete(nome)


class ContaService:

    def create(conta: Conta):
        ContaRepository.create(conta)

    def find_all():
        return ContaRepository.find_all()

    def find_by_numero(numero: str):
        return ContaRepository.find_by_numero(numero)

    def delete(numero: str):
        ContaRepository.delete(numero)
