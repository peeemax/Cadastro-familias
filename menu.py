

# Função de menu de acesso às funções do software:
from cadastro_familia import Familia


def exibir_menu():
    opcao = int(input('''Digite o número de sua opção para acessar:
    1 - Cadastrar uma família
    2 - Listar familias cadastradas
    3 - Procurar dados de uma familia
    '''))

    if opcao == 1:
        Familia(input())
    else:
        print('errado')

exibir_menu()


