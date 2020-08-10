usuarios = ['admin','philipe','lucas','carol','pedro']
	for usuario in usuarios:
		if usuario == 'Admin':
			print('Olá Admin, gostaria de ver um relatório de status?')
		else:
			print('Olá ' + usuario.title() + ' obrigado por fazer fazer login novamente')