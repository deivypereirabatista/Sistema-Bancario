# Sistema Bancário - Projeto de Estudo em Python (POO)

## Objetivo

Desenvolver um sistema bancário utilizando Programação Orientada a Objetos (POO) em Python.

O sistema será executado pelo terminal e deverá permitir o gerenciamento de contas bancárias através de operações básicas.

Este projeto tem como objetivo praticar:

- Classes e Objetos
- Encapsulamento
- Composição
- Organização de código em múltiplos arquivos
- Métodos e atributos
- Regras de negócio
- Estruturação de projetos Python

---

# Contexto

Uma pequena instituição financeira deseja um sistema simples para gerenciamento de contas bancárias.

A primeira versão será executada apenas pelo terminal e armazenará os dados em memória.

Não será utilizado banco de dados nesta etapa.

---

# Funcionalidades

## 1. Criar Conta

O sistema deverá permitir o cadastro de uma nova conta.

### Dados necessários

- Nome do cliente
- CPF
- Número da conta

### Regras

- Toda conta inicia com saldo igual a `0.00`
- Não pode existir mais de uma conta com o mesmo número

---

## 2. Depositar

Permitir depósito em uma conta existente.

### Regras

- O valor deve ser maior que zero
- O saldo deve ser atualizado após o depósito

### Não permitir

- Valor igual a zero
- Valor negativo

---

## 3. Sacar

Permitir saque em uma conta existente.

### Regras

- O valor deve ser maior que zero
- O cliente deve possuir saldo suficiente

### Não permitir

- Valor igual a zero
- Valor negativo
- Saque maior que o saldo disponível

---

## 4. Transferir

Permitir transferência entre duas contas.

### Regras

- Conta de origem deve existir
- Conta de destino deve existir
- Conta de origem deve possuir saldo suficiente

### Resultado esperado

O valor deve ser debitado da conta de origem e creditado na conta de destino.

---

## 5. Consultar Saldo

Exibir informações da conta.

### Informações exibidas

- Nome do cliente
- Número da conta
- Saldo atual

---

## 6. Listar Contas

Exibir todas as contas cadastradas.

### Informações exibidas

- Número da conta
- Nome do cliente
- Saldo

---

# Menu Principal

```text
======== BANCO ========

1 - Criar Conta
2 - Depositar
3 - Sacar
4 - Transferir
5 - Consultar Saldo
6 - Listar Contas
0 - Sair

Escolha:
```

---

# Requisitos Técnicos

## Obrigatório

- Utilizar Programação Orientada a Objetos
- Utilizar classes
- Separar responsabilidades entre as classes
- Organizar o código em múltiplos arquivos
- Utilizar métodos para as operações do sistema

---

# Estrutura Sugerida

```text
projeto_banco/

├── main.py
├── banco.py
├── conta.py
└── cliente.py
```

---

# Classes Mínimas Esperadas

## Cliente

Responsável pelos dados do cliente.

### Definir

- Atributos
- Construtor
- Métodos necessários

---

## Conta

Responsável pelas operações bancárias.

### Deve possuir operações para

- Depositar
- Sacar
- Transferir
- Consultar saldo

---

## Banco

Responsável pelo gerenciamento das contas.

### Deve permitir

- Adicionar contas
- Buscar contas
- Listar contas
- Validar contas existentes

---

# Antes de Programar

Realizar a modelagem do sistema respondendo:

## Cliente

- Quais atributos terá?

## Conta

- Quais atributos terá?
- Quais métodos terá?

## Banco

- Como as contas serão armazenadas?
- Lista?
- Dicionário?
- Outra estrutura?

Justificar a escolha.

---

# Critérios de Avaliação

Ao finalizar o projeto, verificar:

## Organização

- Cada classe possui uma responsabilidade clara?

## Encapsulamento

- Os métodos estão na classe correta?

## Legibilidade

- Os nomes de variáveis, métodos e classes são claros?

## Reutilização

- Existe código duplicado que poderia ser reaproveitado?

## Validações

- As regras de negócio estão sendo respeitadas?

## Estrutura

- O projeto está organizado em arquivos separados?

---

# Sprint 2 (Após concluir a primeira versão)

Implementar:

- Extrato bancário
- Histórico de transações
- Conta Corrente
- Conta Poupança
- Persistência em JSON

---

# Sprint 3 (Desafio)

Implementar:

- Repository Pattern
- Service Layer
- Persistência em SQLite
- Interface gráfica ou API com FastAPI

---

# Objetivo Final

Criar um sistema bancário funcional aplicando corretamente os fundamentos de Programação Orientada a Objetos e preparando a base para projetos maiores no futuro.

---

# Progresso

- [ ] Criar classe Cliente
- [ ] Criar classe Conta
- [ ] Criar classe Banco
- [ ] Implementar criação de contas
- [ ] Implementar depósito
- [ ] Implementar saque
- [ ] Implementar transferência
- [ ] Implementar consulta de saldo
- [ ] Implementar listagem de contas
- [ ] Testar todas as funcionalidades
- [ ] Refatorar código
