nome = 'philipe'

if(nome == 'philipe'):
	print('True, '+nome.title())
if(nome != 'carol'):
	print('True, nome não é Carol')
if(nome.title() == 'Philipe'):
	print('True o nome esta igual a '+nome.title()) 

number_1 = 18
number_2 = 20

if(number_1 > 17):
	print('O numero de maior de 17')
if(number_2 < 17):
	print('O numero de menor que 17')

if(number_1 >= 18):
	print('O numero de maior igual de 18')

if(number_2 <= 18):
	print('O numero de menor igual de 17')

if(number_1 >18) and (number_2 <20):
	print('true')

if(number_1 >18) or (number_2 <20):
	print('true')

nomes = ['Laís','Carol','Lucas','Pedro']
nome = 'Pedro' 
if nome in nomes:
	print('Esse nomes esta na lista de nome: '+nome.title())
nome = 'João'
if nome not in nomes:
	print('Esse nome não esta na lista de nome: '+nome.title())