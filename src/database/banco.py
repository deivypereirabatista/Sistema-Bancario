from models.cliente import Cliente
from models.conta import Conta
from models.transacao import Transacao

clientes: list[Cliente] = []
contas: list[Conta] = []
transacoes: list[Transacao] = []

proximo_numero_conta = 1

def gerar_numero_conta():
    global proximo_numero_conta

    numero = proximo_numero_conta
    proximo_numero_conta += 1

    return numero

def gerar_agencia_conta():
    return 1010

    