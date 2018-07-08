class Pessoa:
    # Atributos
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # Método cumprimentar
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(p.nome, p.idade)
    p.nome = 'Nataly'
    p.idade = 24
    print(p.nome, p.idade)