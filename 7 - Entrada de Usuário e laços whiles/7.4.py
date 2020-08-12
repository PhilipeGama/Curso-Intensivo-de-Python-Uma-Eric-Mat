prompt = "\nEscolha os ingredientes para a pizza"
prompt += "\nDigite 'quit' para sair: "
ingrediente = ""
while ingrediente != 'quit':
	ingrediente = input(prompt)

	print(ingrediente.title() +  " foi adicionado a sua pizza")