from repositories.cliente_repository import ClienteRepository
from models.cliente import Cliente

class ClinteService:

    def create(cliente: Cliente):
        ClienteRepository.create(cliente)

    def find_all(): 
        return ClienteRepository.find_all()
        

    def find_by_nome(nome:str):
        return  ClienteRepository.find_by_nome(nome)
        

    def update(novo_cliente: Cliente, nome: str):
        ClienteRepository.update(nome)

    def delete(nome: str):
        ClienteRepository.delete(nome)



