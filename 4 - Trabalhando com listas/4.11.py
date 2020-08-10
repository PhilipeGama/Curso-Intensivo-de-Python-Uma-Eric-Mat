my_pizzas = ['calabresa','portuguesa','mussarela']
friends_pizzas = my_pizzas[:]
friends_pizzas.append('bacon')

print("Minha pizzas favoritas são:")
for pizza in my_pizzas:
	print(pizza)

print("As pizza favoritas de meu amigo são:")
for pizza in friends_pizzas:
	print(pizza)