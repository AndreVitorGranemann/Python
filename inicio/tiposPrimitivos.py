#Tipos primitivos no python
#int (para numeros inteiros), str(String), bool(verdadeiro  ou falso),float(numeros com virgula)

# no python não é necessário definir o tipo, o mesmo ja e identificado conforme seus caracteres
idade = 24
nome = "Andre"
verdade = True
salario  =  3800.90
#print(nome da variavel) imprime o valor atribuido a cada variavél
print(idade)
print(nome)
print(verdade)
print(salario)
#print f(nome variavel) imprime o valor de cada variavel definindo assim entre{}.
print(f'{idade} - {nome} - {verdade} - {salario}')

#print(type(nome da variavél)) imprime o tipo primitivo da variável
print(type(idade))
print(type(nome))
print(type(verdade))
print(type(salario))

# está condição me permite construir cabeçalho sem escrever 20 o caracter = apenas com 10*
print('='*10, 'Sistema de cadastro', '='*10)

# Python sobrescreve a memoria, se a variavel obter o mesmo nome
nome = 'Andre'
nome = 15
nome = True
nome = 15.8
#print(nome) irá exibir apenas 15.8 devido a sobresscrita de variavél
print(nome)


