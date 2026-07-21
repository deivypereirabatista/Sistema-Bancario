from services.banco_service import ClinteService
from models.cliente import Cliente
from database.banco import gerar_numero_conta


def menu_inicial():
    print("==========Sistema Bancário==========")
    print("Digite 1 para Criar Cadastro: ")
    print("Digite 2 para Criar Conta: ")
    print("Digite 3 para Realizar Transações: ")
    print("Digite 4 para Sair: ")

def exibir_menu_cliente():
    
    print("Digite 1 para Criar Cadastro: ")
    print("Digite 2 para Listar Todas os Cliente: ")
    print("Digite 3 para Listar por Nome: ")
    print("Digite 4 para Atualizar Cadastro: ")
    print("Digite 5 para Deletar Cadastro: ")
    print("Digite 6 para Sair: ")

def exibir_menu_conta():
    
    print("Digite 1 para Criar Conta: ")
    print("Digite 2 para Listar Todas os Contas: ")
    print("Digite 3 para Listar por Numero da Conta: ")
    print("Digite 4 para Deletar Conta: ")
    print("Digite 5 para Sair: ")

def iniciar():
    while True:
        menu_inicial()
        escolha_inical = int(input('Digite o número correspondente a ação: '))

        if escolha_inical == 1:
            while True:
                exibir_menu_cliente()

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
                    nome_titular = input('Digite o nome do Titular da conta: ')
                    if nome_titular:
                        ClinteService.delete(nome_titular)
                    else:
                        print('Cliente não encontrado.')

                if escolha == 6: 
                    break


        if escolha_inical == 2:
            while True:
                exibir_menu_conta()

                if escolha == 1:
                    numero = gerar_numero_conta()
                    

        
        if escolha_inical == 4:
            break