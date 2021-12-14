#variavel lista1 recebe lista vazia
lista1 = []
#variavel lista1 permite inserir valores
#input solicita ao usuario atribuir valores a lista
lista1.append(input('Digite o seu nome:'))
lista1.append(input('Digite o seu nome:'))
print(lista1)
#variavel lista1 recebe função oculta .remove() e atribuimos valor especifico a ser excluido
lista1.remove('valor inserido lista')
print(lista1)
nome = lista1.pop(0)