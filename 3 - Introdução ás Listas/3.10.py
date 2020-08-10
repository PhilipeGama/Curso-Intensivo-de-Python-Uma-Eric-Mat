lista_jogos = ['metal gear 3','resident evil 4','fallout 4','gta 5','demon creed']
lista_jogos.append('donkey kong 1')
lista_jogos.insert(0,'crisis 3')
print(lista_jogos)
del lista_jogos[2]
print(lista_jogos)
jogo_kojima = lista_jogos.pop(1)
print('A Hideo Kojima Game '+jogo_kojima.title())
print('Tamanho da lista de jogos '+str(len(lista_jogos)))
print(sorted(lista_jogos))
print(sorted(lista_jogos,reverse=True))
lista_jogos.sort();
print(lista_jogos)
lista_jogos.reverse()
print(lista_jogos)