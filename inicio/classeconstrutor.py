#classe com nome Pessoa sem nenhum atributo a classe em questão
class Pessoa:   

# def função, init construtor, recebendo atravez de self os atributos da classe
#os atributos estão inseridos no construtor
    def __init__(self, nome, sobrenome, idade):
#self.atributo = atributo aqui estamos falando que o atributo do construor recebe variavel de acesso
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
#def função  str metodo oculto,(self) padrão de acesso
#return f retorno recebe valoresf'{self.nome}' este nome é a variavel do atributo do construtor
    def __str__(self):
        return f'{self.nome}-{self.sobrenome}-{self.idade}'

#p1 objeto de Pessoa, recebendo direto os valores ao obejeto p1 da classe pessoa
#p1 objeto de Pessoa irá imprimiros valores conforme foi definido na função __str__
p1 = Pessoa('Andre', 'Granemann',25)
print(p1)