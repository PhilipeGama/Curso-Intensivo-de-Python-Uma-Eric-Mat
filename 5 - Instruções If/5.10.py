current_users = ['admin','philipe','giovanna','lais','pedro']
new_users = ['joão','philipe','joed','thiago','paulo']

for new_user in new_users:
	if new_user in current_users:
		print('Nome esta disponível')
	else:
		print('Nome não esta disponível')
