prompt = "\nEscolha os ingredientes para a pizza"
prompt += "\nDigite 'quit' para sair: "
ingrediente = ""
active = True

while active:
	ingrediente = input(prompt)
	if ingrediente == "quit":
		active = False
		break
	print(ingrediente.title() +  " foi adicionado a sua pizza")
