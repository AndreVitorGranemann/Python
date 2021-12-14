# def significa função na função soma atribuimos variaveis de nome n1, n2
#return n1 + n2 é o retorno do calculo atribuido a variavel soma
def soma(n1, n2):
    return n1 + n2

# def função, sub variavel recebendo três atributos n1, n2, n3=0.
# neste exemplo temos um atributo opcional onde o terceiro atributo pode ou não ser declarado
def sub(n1, n2, n3=0): #função opcional
    return n1 - n2 - n3
#variavel resultado recebe função soma, inserindo valores aos atributos
resultado = soma(10, 20.8)
print(resultado)

#variavel resultado recebe função sub inserindo valores aos atributos
#este exemplo não foi declarado terceiro atributo, que é opcional
resultado = sub(10, 15)
print(resultado)

#variavel resultado recene função sub inserindo valores aos trez atributos declarados
resultado = sub(10, 15, 20)
print(resultado)

#variavel resultado recebe a função sub definindo os atributos e valores na ordem desejada
resultado = sub(n2=10, n1=20)
print(resultado)