from services.banco_service import ClinteService

def exibir_menu():
    print("==========Sistema Bancário==========")
    print("Digite 1 para Criar conta: ")
    print("Digite 2 para Listar Todas as Contas: ")
    print("Digite 3 para Listar por Nome: ")
    print("Digite 4 para Atualizar Conta: ")
    print("Digite 5 para Deletar conta: ")
    print("Digite 6 para Sair: ")

while True:
    exibir_menu()

    escolha = int(input('Deigite o número correspondente a ação: '))

    if escolha == 1:
        ClinteService.create()
    if escolha == 2:
        ClinteService.find_all()
    if escolha == 3:
        ClinteService.find_by_nome()
    if escolha == 4:
        ClinteService.update()
    if escolha == 5:
        ClinteService.delete()
    if escolha == 6: 
        break

    