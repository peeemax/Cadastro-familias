# Função de menu de acesso às funções do software:
from cadastro_familia import Familia, Pessoa


def exibir_menu():
    opcao = int(input('''Digite o número de sua opção para acessar:
    1 - Cadastrar uma família
    2 - Listar familias cadastradas
    3 - Procurar dados de uma familia
    '''))

    while opcao == 1 or 2 or 3:

        if opcao == 1:

            deseja_novo_cadastro = 'Sim'

            while deseja_novo_cadastro == 'Sim':

                familia1 = Familia(input('Digite o sobrenome da familia: '),
                                   input('Digite o Endereço da residência, com a cidade e estado separado por (-):'),
                                   input('Digite a quantidade de membros da familia:'),
                                   (Pessoa(input('Digite o nome completo do membro?'),
                                          input('Digite a data de nascimento. (DD/MM/AAAA)'),
                                          input('Digite a idade (somente numeros).'),
                                          input('Digite o CPF. (somente numeros)'))))

                print(familia1.nome, familia1.endereco, familia1.qtd_membros, familia1.membros)

                deseja_novo_cadastro = input('Deseja fazer um novo cadastro de familia? (Digite Sim/Não)')

                if deseja_novo_cadastro == 'Sim':
                    familia2 = Familia(input('Digite o sobrenome da familia: '),
                                       input(
                                           'Digite o Endereço da residência, com a cidade e estado separado por (-):'),
                                       input('Digite a quantidade de membros da familia:'),
                                       input('Digite o nome dos membros, separado por vírgula: '))

                    print(familia2.nome, familia2.endereco, familia2.qtd_membros, familia2.membros)

                    deseja_novo_cadastro = input('Deseja fazer um novo cadastro de familia? (Digite Sim/Não)')

                    print('Obrigado')

        elif opcao == 2:

            print(familia1.nome, familia1.endereco, familia1.qtd_membros, familia1.membros)

            print(familia2.nome, familia2.endereco, familia2.qtd_membros, familia2.membros)


        elif opcao == 3:

            print('Fazer a busca')

        opcao = int(input('''Digite o número de sua opção para acessar:
            1 - Cadastrar uma família
            2 - Listar familias cadastradas
            3 - Procurar dados de uma familia
            4 - Sair
            '''))

        if opcao == 4:
            break


exibir_menu()
