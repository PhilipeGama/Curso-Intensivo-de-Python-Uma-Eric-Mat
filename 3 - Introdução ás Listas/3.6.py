lista_convidado = ['carol','roberto','ruan']
pessoa_removida = lista_convidado.pop(2)
lista_convidado.append('marcelo')
lista_convidado.insert(0,'victor')
lista_convidado.insert(1,'raissa')
lista_convidado.append('lucas')
print(lista_convidado[0].title()+', gostaria de jantar comigo?')
print(lista_convidado[1].title()+', gostaria de jantar comigo?')
print(lista_convidado[2].title()+', gostaria de jantar comigo?')
print(lista_convidado[3].title()+', gostaria de jantar comigo?')
print(lista_convidado[4].title()+', gostaria de jantar comigo?')
print(lista_convidado[5].title()+', gostaria de jantar comigo?')
print(pessoa_removida.title()+' não podera comparecer')
print("Encontrei uma mesa de jantar maior")
