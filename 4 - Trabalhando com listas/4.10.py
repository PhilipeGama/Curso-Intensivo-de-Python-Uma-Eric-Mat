players = ['charles','martina','michael','florence','eli']

first_3_players = players[0:3] 
middle_player = players[2]
last_3_players =  players[-3:]

print("Os três primeiros jogadores")
for player in first_3_players:
	print(player.title())

print("Jogador do meio")
print(middle_player.title())

print("Os três ultimos jogadores")
for player in last_3_players:
	print(player.title())