def descrive_pet(pet_name,animal_type = 'dog' ):
	"""Exibe informações sobre um animal de estimação."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Um cachorro chamamdo Willie
descrive_pet('willie')
descrive_pet(pet_name = 'willie')

# Um hamster chamado Harry
descrive_pet('harry','hamster')
descrive_pet(pet_name ='harry', animal_type='hamster')
descrive_pet(animal_type='hamster', pet_name = 'harry')