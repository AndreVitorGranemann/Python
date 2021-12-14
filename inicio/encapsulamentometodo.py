#classe com nome Pessoa sem nenhum atributo a classe em questão
class Pessoa:   
# def função, init construtor, recebendo atravez de self os atributos da classe
#neste exemplo temos atributos privados

    def __init__(self, nome, sobrenome, idade):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade

#metodos getter e setter

    def getNome(self):
        return self.__nome    
    
    def setNome(self, nome):
        self.__nome = nome

    def getSobrenome(self):
        return self.__sobrenome  

    def setSobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    def getIdade(self):
        return self.__idade  

    def setIdade(self, idade):
        self.__idade = idade    
        
#def função str(self) função anonima que recebe um atributo por padrao
#acessando assimos atributos privados do construtor atraves dos metodos get, set 
    def __str__(self):
        return f'{self.__nome}-{self.__sobrenome}-{self.__idade}'

#p1 variavel = Pessoa() variavel p1 recebe a classe pessoa
#permitindo assim definir valores aos atributos vazios da classe
p1 = Pessoa('Andre', 'Granemann',25)
#p1.getIdade permite acessar o methodo get do atributo idade
print(p1.getIdade())

#variavel idade recebe inteiro, input solicita ao usuario atribuir valor do tipo int
idade = int(input('Digite a nova idade:'))
#p1 objeto de pessoa recebe setIdade atribuindo valor davariavel idade que foi solicitado ao usuario
p1.setIdade(idade)
print(p1.getIdade())