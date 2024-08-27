import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sua_senha",
        database="banco_bancario"
    )

def criar_correntista(nome, cpf, endereco):
    conexao = conectar_db()
    cursor = conexao.cursor()
    sql = "INSERT INTO correntistas (nome, cpf, endereco) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, cpf, endereco))
    conexao.commit()
    conexao.close()

def criar_conta(numero_conta, saldo, correntista_id):
    conexao = conectar_db()
    cursor = conexao.cursor()
    sql = "INSERT INTO contas (numero_conta, saldo, correntista_id) VALUES (%s, %s, %s)"
    cursor.execute(sql, (numero_conta, saldo, correntista_id))
    conexao.commit()
    conexao.close()

def realizar_deposito(conta_id, valor):
    conexao = conectar_db()
    cursor = conexao.cursor()
    sql = "UPDATE contas SET saldo = saldo + %s WHERE id = %s"
    cursor.execute(sql, (valor, conta_id))
    conexao.commit()
    conexao.close()

def realizar_saque(conta_id, valor):
    conexao = conectar_db()
    cursor = conexao.cursor()
    sql = "UPDATE contas SET saldo = saldo - %s WHERE id = %s"
    cursor.execute(sql, (valor, conta_id))
    conexao.commit()
    conexao.close()

def gerar_extrato(conta_id):
    conexao = conectar_db()
    cursor = conexao.cursor()
    sql = "SELECT * FROM movimentacoes WHERE conta_id = %s ORDER BY data_movimentacao DESC"
    cursor.execute(sql, (conta_id,))
    extrato = cursor.fetchall()
    conexao.close()
    return extrato
