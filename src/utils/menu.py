from services.banco_service import ClinteService
from models.cliente import Cliente

def exibir_menu():
    print("==========Sistema Bancário==========")
    print("Digite 1 para Criar conta: ")
    print("Digite 2 para Listar Todas as Contas: ")
    print("Digite 3 para Listar por Nome: ")
    print("Digite 4 para Atualizar Conta: ")
    print("Digite 5 para Deletar conta: ")
    print("Digite 6 para Sair: ")

def iniciar():
    while True:
        exibir_menu()

        escolha = int(input('Deigite o número correspondente a ação: '))

        if escolha == 1:
            nome = input('Digite o Nome do Titular da conta: ')
            cpf = input('Digite o CPF do Titular da conta: ')
            data_nascimento = input('Digite a Data de Nascimento do Titular da conta: ')
            endereco = input('Digite o endereco do Titular da conta: ')

            ClinteService.create(cliente = Cliente(
                nome=nome,
                cpf=cpf,
                data_nascimento=data_nascimento,
                endereco=endereco
            ))

        if escolha == 2:
            clientes = ClinteService.find_all()

            for cliente in clientes:
                print(cliente)
            
        if escolha == 3:
            nome = input('Digite o nome do Titular da conta: ')
            cliente = ClinteService.find_by_nome(nome)
            if cliente:
                print(cliente)
            else:
                print('Cliente não econtrado.')

                
        if escolha == 4:
            nome_titular = input('Digite o nome do Titular: ')
            if nome_titular:
                novo_nome = input('Digite um novo Nome: ')
                novo_cpf = input('Digite o novo CPF: ')
                novo_data_nascimento = input('Digite a nova Data de Nascimento: ')
                novo_endereco = input('Digite o novo Endereço: ')
                ClinteService.update(nome, Cliente(
                    nome=novo_nome,
                    cpf=novo_cpf,
                    data_nascimento=novo_data_nascimento,
                    endereco=novo_endereco
                ))
            


        if escolha == 5:
            ClinteService.delete()

        if escolha == 6: 
            break

    