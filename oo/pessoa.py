class Pessoa:
    # Atributos
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        # Atributo complexo 'filhos'
        self.filhos = list(filhos)

    # Método cumprimentar
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    # Objeto comum - instância da classe Pessoa
    filho = Pessoa(nome='Giancarlo', idade=34)

    # Objeto com atributo complexo
    mae = Pessoa(filho, nome='Bernadete', idade=18)

    print(filho.nome)
    print(mae.nome)

    # Atributo dinâmico 'sobrenome', adicionado ao objeto 'filho' em tempo de execução
    filho.sobrenome = "Silva"
    print(filho.nome, filho.sobrenome)