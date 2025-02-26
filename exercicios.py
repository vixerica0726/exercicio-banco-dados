import sqlite3  # Importando o módulo sqlite3

conexao = sqlite3.connect('exerciciosbancodedados.db')
cursor = conexao.cursor()  # Criando um cursor
print('Conexão realizada com sucesso!')
     

# 1. Criar a tabela chamada "alunos" com os campos: id, nome, idade e curso.
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    curso TEXT NOT NULL
)
""")
print("Tabela criada com sucesso!")
     

# 2. Inserir 5 registros de alunos na tabela "alunos"
alunos = [
    ("Nathan Felix", 23, "Engenharia"),
    ("David Pin", 25, "Marketing"),
    ("Erica Oliveira", 19, "Análise de dados"),
    ("Martha Souza", 36, "Enfermagem"),
    ("Clarice Santos", 22, "Administração"),
    ("Allan", 31, "Mecânica")
]
# Inserir os dados na tabela 'alunos'
cursor.executemany('INSERT INTO alunos(nome, idade, curso) VALUES (?, ?, ?)', alunos)
print("Dados inseridos com sucesso!")
     

# 3. Consultas Básicas
# a) Mostrar todos os alunos
print("Todos os alunos:")
visualizar = cursor.execute('SELECT * FROM alunos')
for aluno in visualizar:
    print(aluno)

# b) Alunos com mais de 20 anos
print("\nAlunos com mais de 20 anos:")
maiorIdade = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for aluno in maiorIdade:
    print(aluno)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
print('\nAlunos engenharia')
curso = cursor.execute("SELECT * FROM alunos WHERE curso LIKE '%Engenharia%' ORDER BY nome;")
for aluno in curso:
    print(aluno)

# d) Contar o número total de alunos na tabela
print('\n Número total de alunos')
total = cursor.execute('SELECT COUNT(*) FROM alunos;')
total_alunos = total.fetchone()[0]  # Obtendo o resultado da contagem
print(f"Total de alunos: {total_alunos}")
     

# 4. Atualização e Remoção

# Atualizando a idade de um aluno específico
idade_atual = 23  # Idade que será atualizada
nova_idade = 25  # Nova idade

cursor.execute('UPDATE alunos SET idade = ? WHERE idade = ?', (nova_idade, idade_atual))
conexao.commit()

print("Idade do aluno atualizada com sucesso!")

     

# b) Remova um aluno pelo seu ID.
# Removendo um aluno pelo ID
id_aluno = 3  # ID do aluno a ser removido

cursor.execute('DELETE FROM alunos WHERE id = ?', (id_aluno,))
conexao.commit()

print(f"Aluno com ID {id_aluno} removido com sucesso!")

     

# 5. Criar uma Tabela e Inserir Dados
# Criar a tabela "clientes" com os campos: id, nome, idade e saldo
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    saldo FLOAT NOT NULL
)
""")
conexao.commit()  # Confirma a criação da tabela

# Inserir registros na tabela "clientes"
clientes = [
    ("Lucas Silva", 30, 5000.75),
    ("Maria Oliveira", 45, 3500.50),
    ("José Santos", 29, 1500.20),
    ("Ana Costa", 55, 10000.00),
    ("Paulo Almeida", 40, 2200.10)
]

cursor.executemany('INSERT INTO clientes (nome, idade, saldo) VALUES (?, ?, ?)', clientes)
conexao.commit()  # Confirma a inserção dos registros

print('Tabela "clientes" criada e dados inseridos com sucesso!')

     

# 6. Consultas e Funções Agregadas
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
resultado = cursor.fetchall()
for cliente in resultado:
    print(cliente)
     

# b) Calcule o saldo médio dos clientes.
print("\nb) Saldo médio dos clientes:")
cursor.execute('SELECT AVG(saldo) FROM clientes')
saldo_medio = cursor.fetchone()[0]  # Pegando o resultado da média
print(f"Saldo médio: {saldo_medio:.2f}")
     

# c) Encontre o cliente com o saldo máximo
print("\nc) Cliente com o saldo máximo:")
cursor.execute('SELECT nome, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
cliente_max_saldo = cursor.fetchone()
print(cliente_max_saldo)
     

# d) Contar quantos clientes têm saldo acima de 1000
print("\nd) Número de clientes com saldo acima de 1000:")
cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
num_clientes = cursor.fetchone()[0]  # Pegando o número de clientes
print(f"Total de clientes com saldo acima de 1000: {num_clientes}")
     

# a) Atualizar o saldo de um cliente específico
id_cliente = 3  # ID do cliente para o qual vamos atualizar o saldo
novo_saldo = 3000.00  # Novo valor do saldo

cursor.execute('UPDATE clientes SET saldo = ? WHERE id = ?', (novo_saldo, id_cliente))

# b) Remover um cliente pelo seu ID
id_cliente_remover = 2  # ID do cliente a ser removido

cursor.execute('DELETE FROM clientes WHERE id = ?', (id_cliente_remover,))
print("Cliente removido com sucesso!")
     

import sqlite3

# Conectar ao banco de dados (substitua 'exerciciosbancodedados.db' pelo nome do seu banco de dados)
conn = sqlite3.connect('exerciciosbancodedados.db')
cursor = conn.cursor()

# 1. Criar a tabela 'clientes' com os campos: id, nome, idade e saldo
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    saldo FLOAT NOT NULL
);
""")
conn.commit()  # Confirma a criação da tabela

# Inserir registros na tabela "clientes"
clientes = [
    ("Lucas Silva", 30, 5000.75),
    ("Maria Oliveira", 45, 3500.50),
    ("José Santos", 29, 1500.20),
    ("Ana Costa", 55, 10000.00),
    ("Paulo Almeida", 40, 2200.10)
]
cursor.executemany('INSERT INTO clientes (nome, idade, saldo) VALUES (?, ?, ?)', clientes)
conn.commit()  # Confirma a inserção dos registros
print('Tabela "clientes" criada e dados inseridos com sucesso!')

# 2. Criar a tabela 'compras' (caso não exista)
cursor.execute("""
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    valor REAL NOT NULL,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
""")
conn.commit()  # Confirma a criação da tabela

# Inserir registros na tabela "compras"
compras = [
    ("Produto A", 150.75, 1),  # Produto A comprado por Lucas Silva (id=1)
    ("Produto B", 200.30, 2),  # Produto B comprado por Maria Oliveira (id=2)
    ("Produto C", 99.90, 3),   # Produto C comprado por José Santos (id=3)
    ("Produto D", 350.40, 4),  # Produto D comprado por Ana Costa (id=4)
    ("Produto E", 120.10, 5)   # Produto E comprado por Paulo Almeida (id=5)
]
cursor.executemany('INSERT INTO compras (produto, valor, cliente_id) VALUES (?, ?, ?)', compras)
conn.commit()  # Confirma a inserção dos registros
print('Tabela "compras" criada e dados inseridos com sucesso!')

# 3. Realizar a consulta: Nome do Cliente, Produto e Valor da Compra
print("\nConsulta: Nome do Cliente, Produto e Valor da Compra")
cursor.execute("""
SELECT clientes.nome, compras.produto, compras.valor
FROM compras
JOIN clientes ON compras.cliente_id = clientes.id;
""")
result = cursor.fetchall()

# Exibir o resultado da consulta
for row in result:
    print(row)

# Fechar a conexão
conn.close()
