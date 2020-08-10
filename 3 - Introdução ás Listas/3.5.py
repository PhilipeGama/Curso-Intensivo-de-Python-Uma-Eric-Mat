lista_convidado = ['carol','roberto','ruan']
print(lista_convidado[0].title()+', gostaria de jantar comigo?')
print(lista_convidado[1].title()+', gostaria de jantar comigo?')
pessoa_removida = lista_convidado.pop(2)
lista_convidado.append('marcelo')
print(lista_convidado[2].title()+', gostaria de jantar comigo?')
print(pessoa_removida.title()+' não podera comparecer')
