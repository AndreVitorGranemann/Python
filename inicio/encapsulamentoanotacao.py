#classe com nome Pessoa sem nenhum atributo a classe em questão
class Pessoa:   
# def função, init construtor, recebendo atravez de self os atributos da classe
#neste exemplo temos atributos privados
    def __init__(self, nome, sobrenome, idade):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
    
#aqui temos @property que é uma anotação de propriedade como se fosse um get 
#aqui temos @nome.setter que é uma anotação com nome da função.setter

    @property
    def nome(self):
        return self.__nome    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sobrenome(self):
        return self.__sobrenome  

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    @property
    def idade(self):
        return self.__idade  
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade     
#def função str(self) função anonima que recebe um atributo por padrao
#acessando assimos atributos privados do construtor atraves das anotaçoes @nomefunção.setter @property

    def __str__(self):
        return f'{self.__nome}-{self.__sobrenome}-{self.__idade}'


#p1 variavel = Pessoa() variavel p1 recebe a classe pessoa
#permitindo assim definir valores aos atributos vazios da classe
p1 = Pessoa('Andre', 'Granemann',25)
print(p1.nome)
#p1 objeto de pessoa recebe setIdade atribuindo valor davariavel idade que foi solicitado ao usuario
p1.idade = int(input('Digite a nova idade:'))
print(p1.idade)