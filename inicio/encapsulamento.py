#classe com nome Pessoa sem nenhum atributo a classe em questão
class Pessoa:   
# def função, init construtor, recebendo atravez de self os atributos da classe
#neste exemplo temos atributos privados
    def __init__(self, nome, sobrenome, idade):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        
#def função str(self) função anonima que recebe um atributo por padrao
#acessando assim os atributos privados do construtor
    def __str__(self):
        return f'{self.__nome}-{self.__sobrenome}-{self.__idade}'

#p1 variavel = Pessoa() variavel p1 recebe a classe pessoa
#permitindo assim definir valores aos atributos vazios da classe

p1 = Pessoa('Andre', 'Granemann',25)
#print(p1) irá imprimir todos os valores definidos no objeto p1 da classe pessoa
print(p1)