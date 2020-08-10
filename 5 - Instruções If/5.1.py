car = 'subaru'

if car == 'subaru':
	print('O carro é o '+car.title())
else:
	print('O carro não é o '+car.title())

	
car = 'subaru'
if car == 'Subaru':
	print('O carro é o '+car.title()+ "é esta escrito corretamente")
if car == 'subaru':
	print('O carro é o '+car+ " está escrito em minusculo")


number_1 = 18
if(number_1 > 18):
	print('Este numero é maior que 18')

if (number_1 >= 18):
	print('Este numero é maior ou igual a dezoito')	

number_2 = 23
if(number_2 == 23) or (number_2 < 25):
	print('Resultado verdadeiro')

nomes = ['Philipe','Carol','Laís']
nome = 'Carol'
if nome in nomes:
	print('Esse nome esta entre os nomes: '+nome)
else:
	print('Não esta entre os nomes')

number_2 = 200
if (number_2 <= 200):
	print('Esse numero é menor ou igual a 200')
else:
	print('Esse numero é maior que 200')