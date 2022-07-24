

# Função de menu de acesso às funções do software:
def exibir_menu():
    opcao = int(input('''Digite o número de sua opção para acessar:
    1 - Cadastrar uma família
    2 - Listar familias cadastradas
    3 - Procurar dados de uma familia
    '''))

    if opcao == 1:
        print('Cadastrar')
    else:
        print('errado')

exibir_menu()
