class Pessoa:
    # Atributo de classe (também chamado de Atributo "default"). Deve ser usado se o valor for igual para
    # todas as instâncias da classe.
    olhos = 2

    # Atributos
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        # Atributo complexo 'filhos'
        self.filhos = list(filhos)

    # Método cumprimentar
    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    # Método de classe, que independe do objeto e por isso não precisa receber nenhum atributo (não há 'self').
    # Para criar, utiliza-se um decorator chamado @staticmethod ou
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - Olhos: {cls.olhos}'

# Classe 'Homem', que herda os atributos e métodos da superclasse 'Pessoa'
class Homem(Pessoa):
    def cumprimentar(self):
        # Sobrescrita de método
        cumprimentar_classe_pai = super().cumprimentar()
        return f'{cumprimentar_classe_pai}. Aperto de mão'

class Mutante(Pessoa):
    # Sobrescrita de atributo
    olhos = 3

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

    # Atributos de classe "olhos"
    print(Pessoa.olhos)
    print(filho.olhos)
    print(mae.olhos)

    # Chamando os métodos estáticos
    print(Pessoa.metodo_estatico())
    print(filho.metodo_estatico())

    print(Pessoa.nome_e_atributos_de_classe())
    print(filho.nome_e_atributos_de_classe())

    irmao = Homem(nome='Eduardo', idade=37)

    print(irmao.nome)

    print(isinstance(irmao, Pessoa))
    print(isinstance(filho, Pessoa))
    print(isinstance(filho, Homem))

    print(filho.olhos)

    mutante = Mutante(nome='Wolverine', idade=80)

    print(mutante.olhos)

    print(filho.cumprimentar())
    print(mae.cumprimentar())

    print(irmao.cumprimentar())