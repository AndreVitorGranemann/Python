# defindindo classe e o nome, o nome da classe não precisa ser igual ao arquivo
# passando trez variaveis com valores vazios
class Pessoa:
    nome = ''
    sobrenome = ''
    idade = 0

#def função str(self) função anonima que recebe um atributo por padrao
#retorno f{self.nomeatributo} permite esta classe ser acessada por um objeto
    def __str__(self):
        return f'{self.nome}-{self.sobrenome}-{self.idade}'

#p1 variavel = Pessoa() variavel p1 recebe a classe pessoa
#permitindo assim definir valores aos atributos vazios da classe
p1 = Pessoa()
p1.nome = 'Andre'
p1.sobrenome = 'Granemann'
p1.idade = 25
#print(p1) irá imprimir todos os valores definidos no objeto p1 da classe pessoa
print(p1)