CREATE DATABASE banco_bancario;

USE banco_bancario;

-- Tabela para armazenar informações dos correntistas
CREATE TABLE correntistas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    endereco VARCHAR(255)
);

-- Tabela para armazenar informações das contas bancárias
CREATE TABLE contas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_conta VARCHAR(20) UNIQUE NOT NULL,
    saldo DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
    correntista_id INT,
    FOREIGN KEY (correntista_id) REFERENCES correntistas(id)
);

-- Tabela para armazenar movimentações bancárias
CREATE TABLE movimentacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('depósito', 'saque') NOT NULL,
    valor DECIMAL(15, 2) NOT NULL,
    data_movimentacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    conta_id INT,
    FOREIGN KEY (conta_id) REFERENCES contas(id)
);
