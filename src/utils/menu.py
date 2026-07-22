from services.banco_service import ClinteService, ContaService
from models.cliente import Cliente
from models.conta import Conta
from database.banco import gerar_numero_conta, gerar_agencia_conta, clientes, contas


def menu_inicial():
    print("==========Sistema Bancário==========")
    print("Digite 1 para Cadastros: ")
    print("Digite 2 para Contas: ")
    print("Digite 3 para Transações: ")
    print("Digite 4 para Sair: ")

def exibir_menu_cliente():
    print("==========CADASTROS==========")
    print("Digite 1 para Criar Cadastro: ")
    print("Digite 2 para Listar Todas os Cliente: ")
    print("Digite 3 para Listar por Nome: ")
    print("Digite 4 para Atualizar Cadastro: ")
    print("Digite 5 para Deletar Cadastro: ")
    print("Digite 6 para Sair: ")

def exibir_menu_conta():
    print("==========CONTAS==========")
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

                escolha_cliente = int(input('Deigite o número correspondente a ação: '))
                #Criar Cadastro para Cliente
                if escolha_cliente == 1:
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
                # Listar todos os Cadastros 
                if escolha_cliente == 2:
                    clientes = ClinteService.find_all()

                    for cliente in clientes:
                        print(cliente)
                #Listar Cadastro por Nome        
                if escolha_cliente == 3:
                    nome = input('Digite o nome do Titular da conta: ')
                    cliente = ClinteService.find_by_nome(nome)
                    if cliente:
                        print(cliente)
                    else:
                        print('Cliente não econtrado.')

                #Atualizar Cadastro de Cliente        
                if escolha_cliente == 4:
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
                    
                #Deletar Cadastro de Cliente
                if escolha_cliente == 5:
                    nome_titular = input('Digite o nome do Titular da conta: ')
                    if nome_titular:
                        ClinteService.delete(nome_titular)
                    else:
                        print('Cliente não encontrado.')
                # Sair
                if escolha_cliente == 6: 
                    break


        if escolha_inical == 2:
            while True:
                exibir_menu_conta()
                escolha_conta = int(input('Digite o número correspondente a ação: '))
                # Criar conta para Cliente
                if escolha_conta == 1:
                    nome_titular = input('Digite o nome do Titular: ')
                    cliente_encontrado = None
                    clientes = ClinteService.find_all()                  
                    for cliente in clientes:
                        if cliente.nome == nome_titular:
                            cliente_encontrado = cliente
                            break

                    if cliente_encontrado:
                        numero = gerar_numero_conta()
                        agencia = gerar_agencia_conta()
                        conta = Conta(
                            numero=numero,
                            agencia=agencia,
                            cliente=cliente_encontrado
                        )
                        mensagem = ContaService.create(conta)
                        print(mensagem)
                        
                    else:
                        print('Necessário realizar o cadastro de Clinte antes de abrir a conta!')
                        break
                # Listar Todas as Contas do Clietne
                if escolha_conta == 2:
                    cpf_titular = input('Digite o CPF do Titular sem espaços ou caracteres especiais: ')
                    cpf_encontrado = None

                    for cliente in clientes:
                        if cliente.cpf == cpf_titular:
                            cpf_encontrado = cliente
                            break
                        if cpf_encontrado:
                            ContaService.find_by_numero(cpf)
                        else:
                            print('Cadastro não encontrado!')
        #Sair Geral
        if escolha_inical == 4:
            break