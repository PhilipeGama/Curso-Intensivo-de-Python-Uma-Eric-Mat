active = True
pessoas = {}

while active:
	nome = input("Qual é o seu nome: ")
	lugar = input("Se pudesse visitar um lugar no mundo, para onde você iria: ")

	pessoas[nome] = lugar

	check = input("Deseja continue(S/N): ")

	if check == "n":
		break

for name,lugar in pessoas.items():
	print("O lugar favorito de " + name.title() + " é " + lugar.title())


