sandwich_orders = ['x-salada','pastrami','x-bacon','x-tudo']
finished_sandwiches = []
print("Preparando os sandwiches")
while sandwich_orders:
	sandwich_order = sandwich_orders.pop()
	if (sandwich_order == 'pastrami'):
		print('Estamos sem Pastrami!')
	else:
		print(sandwich_order.title() + " pronto!")
		finished_sandwiches.append(sandwich_order)

print("\nOs sandwiches estão prontos")
print(finished_sandwiches)
print()