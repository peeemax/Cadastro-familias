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
