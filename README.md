# Sistema Bancário em Python

Este projeto implementa um sistema bancário simples utilizando Python e MySQL. O código permite gerenciar correntistas e contas bancárias, além de realizar operações básicas como depósitos, saques e geração de extratos.

## Funcionalidades

- **Conexão com Banco de Dados**: Estabelece uma conexão com um banco de dados MySQL.
- **Gerenciamento de Correntistas**:
  - Criar novos correntistas com nome, CPF e endereço.
- **Gerenciamento de Contas**:
  - Criar contas associadas a correntistas.
  - Realizar depósitos e saques em contas.
  - Gerar extratos com histórico de movimentações.

## Pré-requisitos

Antes de executar o código, você precisará ter:

- Python 3.x instalado.
- MySQL Server instalado e em execução.
- A biblioteca `mysql-connector-python` instalada. Você pode instalá-la utilizando o seguinte comando:

```bash
pip install mysql-connector-python
