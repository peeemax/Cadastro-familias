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

    # CRUD

    # CREATE
comando = 'SELECT * FROM cadastro_familia'
cursor.execute(comando)
# conexao.commit()  # Editando banco de dados
resultado = cursor.fetchall()  # Lendo banco de dados
print(resultado)

    # Cncerramento e fechamento do banco
cursor.close()
conexao.close()

