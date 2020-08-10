# Armazena informações sobre uma pizza que está sendo pedida
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms','extra cheese']
}

# Resumo o pedido
print('You ordered a '+ pizza['crust'] + '-crust pizza ' +
	  'with the following toppings: ')

for toppings in pizza['toppings']:
	print('\t'+toppings)