favorita_languages = {
				'jen' : 'python',
				'sarah' : 'c',
				'edward' : 'ruby',
				'phil' : 'python',
			}

for name in sorted(favorita_languages.keys()):
	print(name.title() + ', thank you for taking a poll')


print('\nThe following languanges have been mentioned')
for languange in favorita_languages.values():
	print(languange.title())

print('\nThe following languanges have been mentioned no repeat')
for languange in set(favorita_languages.values()):
	print(languange.title())

