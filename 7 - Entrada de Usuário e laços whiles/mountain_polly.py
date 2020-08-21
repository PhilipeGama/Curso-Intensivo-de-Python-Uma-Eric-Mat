responses = {}

# Define um flag para indicar que a enquete está ativa
polling_active = True

while polling_active:
# Pede o nome da pessoa e a resposta
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")

# Armazena a resposta no dicionário
	responses[name] = response

# Descobre se outra pessoa vai responder à enquente
	repeat = input("Would you like to let another person respond? (yes/no): ")
	if repeat == 'no':
		polling_active = False

# A enquente foi concluida. Mostra os resultados
print("\n--- Poll Results ---")
for name, response in responses.items():
	print("Name " + name.title() + " would like to climb " + response.title() + ".")
	
	
