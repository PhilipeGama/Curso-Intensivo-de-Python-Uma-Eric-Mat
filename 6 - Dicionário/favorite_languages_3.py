favorita_languages = {
				'jen' : 'python',
				'sarah' : 'c',
				'edward' : 'ruby',
				'phil' : 'python'
			}

friends = ['phil','sarah']

for name in favorita_languages.keys():
	print(name.title())

	if name in friends:
		print('Hi '+name.title() +
			', I see your favorite languange is '+favorita_languages[name].title()+ '!')

if 'erin' not in favorita_languages.keys():
	print('Erin, please take our poll')