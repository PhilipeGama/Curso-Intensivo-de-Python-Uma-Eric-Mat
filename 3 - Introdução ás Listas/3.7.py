lista_convidado = ['carol','roberto','ruan']

lista_convidado.append('marcelo')
lista_convidado.insert(0,'victor')
lista_convidado.insert(1,'raissa')
lista_convidado.append('lucas')
convidado_removida = lista_convidado.pop(-1)
print('Desculpe '+convidado_removida.title()+' você não esta mais na lista de convidados')
convidado_removida = lista_convidado.pop(-1)
print('Desculpe '+convidado_removida.title()+' você não esta mais na lista de convidados')
convidado_removida = lista_convidado.pop(-1)
print('Desculpe '+convidado_removida.title()+' você não esta mais na lista de convidados')
convidado_removida = lista_convidado.pop(-1)
print('Desculpe '+convidado_removida.title()+' você não esta mais na lista de convidados')
convidado_removida = lista_convidado.pop(-1)
print('Desculpe '+convidado_removida.title()+' você não esta mais na lista de convidados')

print(lista_convidado[0].title()+', gostaria de jantar comigo?')
print(lista_convidado[1].title()+', gostaria de jantar comigo?')

del lista_convidado[1]
del lista_convidado[0]
print(lista_convidado)