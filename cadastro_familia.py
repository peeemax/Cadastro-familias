from types import prepare_class


class Pessoa:
    def __init__(self, nome, data_nascimento, idade, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.idade = idade


class Familia:
    '''Classe para chamar e registrar a familia'''

    def __init__(self, nome, endereco, qtd_membros, membro_principal=Pessoa):  # Método construtor da classe
        self.nome = nome
        self.endereco = endereco
        self.qtd_membros = qtd_membros
        self.membro_principal = membro_principal


if __name__ == "__main__":
    familia1 = Familia('Maximiano', 'Campinas-SP', '3', '')
    print(familia1)
    print(familia1.nome)

if __name__ == "__main__":
    pessoa1 = Pessoa('Pedro Maximiano', '13/09/1992', '29 anos', '42511753871')
    print(pessoa1)
    print(pessoa1.nome)
