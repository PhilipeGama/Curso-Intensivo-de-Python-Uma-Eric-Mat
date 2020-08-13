prompt = "\nQual á sua idade"
prompt += "\nDigite 'quit' para sair: "
idade = input(prompt)
idade = int(idade)

if idade < 3:
	print("Ingresso gratuito")
if idade >= 3 and idade <= 12:
	print("Ingresso é 10 dólares")
else:
	print("Ingresso é 15 dólares")
