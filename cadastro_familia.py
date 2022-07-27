from types import prepare_class


class Familia:
    '''Classe para chamar e registrar a familia'''
    def __init__(self, nome, endereco, qtd_membros, membros): # Método construtor da classe
        self.nome = nome
        self.endereco = endereco
        self.qtd_membros = qtd_membros
        self.membros = membros
    
    def membros(self):
        membros = list(Pessoa)
    
if __name__ == "__main__":
    familia1 = Familia('Maximiano', 'Campinas-SP', '3')
    print(familia1)


class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, idade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.idade = idade