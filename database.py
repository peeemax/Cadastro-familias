import mysql.connector


# Conexão com o banco e os dados do usuário do banco

conexao = mysql.connector.connect(
    host='localhost',
    user='Maximiano',
    password='Pemax1992',
    database='bdcadastrofamilia',
    )

# Execução dos comandos da conexão
cursor = conexao.cursor()

# Encerramento e fechamento do banco
cursor.close()
conexao.close()

