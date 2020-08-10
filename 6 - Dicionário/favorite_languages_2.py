favorita_languages = {
				'jen' : 'python',
				'sarah' : 'c',
				'edward' : 'ruby',
				'phil' : 'python'
			}

for name,language in favorita_languages.items():
	print(name.title() + "'s favorito language is "+ 
		 language.title() + ".")

for name in favorita_languages.keys():
	print(name.title())

