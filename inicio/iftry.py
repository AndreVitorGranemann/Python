# input permite o usuario digitar o valor da variavel
idade = input('Digite sua idade:')
#print('sua idade é:', idade) imprime a mensagem mais o valor da variavel digitada
print('sua idade é:', idade)

#if/se for verdadeiro/(type/tipo da variavél->(idade) é-> is/ ->inteiro int):
# se for numero inteiro exibe/ print('É inteiro')
# caso não seja exibe/ else: print('Não é inteiro')
     
if(type(idade) is int):
    print('É inteiro')
else:
    print('Não é inteiro')
#try se a variavel idade = int(idade) se idade for igual a idade inteiro
# senão except: print('erro ao converter')
try:
    idade = int(idade)
except:
    print('Erro ao converter')