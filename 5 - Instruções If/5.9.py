usuarios = ['admin','philipe','lucas','carol','pedro']
if( usuarios == [] ):
	print('Precisamos encontra alguns usuarios!')
else:
	for usuario in usuarios:
		if usuario == 'admin':
			print('Olá Admin, gostaria de ver um relatório de status?')
		else:
			print('Olá ' + usuario.title() + ' obrigado por fazer fazer login novamente')