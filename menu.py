# Função de menu de acesso às funções do software:
from cadastro_familia import Familia, Pessoa
from database import conexao


# Menu do sistema


def exibir_menu():
    # Entrada para inicio do sistema
    opcao = int(input('''Digite o número de sua opção para acessar:
    1 - Cadastrar uma família
    2 - Listar familias cadastradas
    3 - Atualizar dados familia
    4 - Deletar familia
    5 - Sair'''))

    # Condição para o menu continuar ou parar
    while opcao == 1 or 2 or 3 or 4:

        import mysql.connector
        conexao = mysql.connector.connect(
            host='localhost',
            user='Maximiano',
            password='Pemax1992',
            database='bdcadastrofamilia',
        )

        cursor = conexao.cursor()

        # Condição da opção de cadastro de familia
        if opcao == 1:

            familia1 = Familia(input('Digite o sobrenome da familia: '),
                               input('Digite o Endereço da residência, com a cidade e estado separado por (-):'),
                               input('Digite a quantidade de membros da familia:'),
                               (Pessoa(input('Digite o nome completo do membro?'),
                                       input('Digite a data de nascimento. (DD/MM/AAAA)'),
                                       input('Digite a idade (somente numeros).'),
                                       input('Digite o CPF. (somente numeros)'))))

            print(familia1.nome, familia1.endereco, familia1.qtd_membros, familia1.membros)

            comando = f'INSERT INTO cadastro_familia (nome_familia, endereco, qtd_membros, membros) VALUES ' \
                      f'("{familia1.nome}", "{familia1.endereco}", "{familia1.qtd_membros}", "{familia1.membros}")'

            cursor.execute(comando)
            conexao.commit()

            opcao = int(input('''Digite o número de sua opção para acessar:
                            1 - Cadastrar uma família
                            2 - Listar familias cadastradas
                            3 - Atualizar dados familia
                            4 - Deletar familia
                            5 - Sair'''))

        # Vizualição das familias do banco de dados
        elif opcao == 2:

            comando = 'SELECT * FROM cadastro_familia'

            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(resultado)

            opcao = int(input('''Digite o número de sua opção para acessar:
                            1 - Cadastrar uma família
                            2 - Listar familias cadastradas
                            3 - Atualizar dados familia
                            4 - Deletar familia
                            5 - Sair'''))

        elif opcao == 3:

            alteracao = input('Digite o nome da familia.')

            update = input('Digite qual dado quer alterar (endereco, qtd_membros ou membros)')

            if update == 'endereco':

                endereco_alterado = input('Digite o novo endereço.')
                comando = f'UPDATE cadastro_familia SET endereco = "{endereco_alterado}" WHERE nome_familia = "{alteracao}"'

                cursor.execute(comando)
                conexao.commit()

            elif update == 'qtd_membros':

                qtd_alterado = input('Digite o nova quantidade de membros.')
                comando = f'UPDATE cadastro_familia SET endereco = "{qtd_alterado}" WHERE nome_familia = "{alteracao}"'

                cursor.execute(comando)
                conexao.commit()

            elif update == 'membros':

                membro_alterado = input('Digite a alteração do membro.')
                comando = f'UPDATE cadastro_familia SET endereco = "{membro_alterado}" WHERE nome_familia = "{alteracao}"'

                cursor.execute(comando)
                conexao.commit()

            opcao = int(input('''Digite o número de sua opção para acessar:
                                            1 - Cadastrar uma família
                                            2 - Listar familias cadastradas
                                            3 - Atualizar dados familia
                                            4 - Deletar familia
                                            5 - Sair'''))

        elif opcao == 4:

            familia = input('Digite o nome da familia que deseja excluir.')
            comando = f'DELETE FROM cadastro_familia WHERE nome_familia = "{familia}"'

            cursor.execute(comando)
            conexao.commit()

        opcao = int(input('''Digite o número de sua opção para acessar:
                                                    1 - Cadastrar uma família
                                                    2 - Listar familias cadastradas
                                                    3 - Atualizar dados familia
                                                    4 - Deletar familia
                                                    5 - Sair'''))

        break

        cursor.close()
        conexao.close()


exibir_menu()
