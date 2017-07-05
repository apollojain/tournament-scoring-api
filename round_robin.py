from operator import itemgetter
import helpers

def is_list(item):
	if isinstance(item, list):
		return True
	else: 
		return False

def switch_games(dictionary):
	dictionary["Side A"].append(dictionary["Side A"].pop(0))

def add_game_to_team(dictionary, team, round, game):
	if team not in dictionary["Teams"]:
		dictionary["Teams"][team] = {}
	dictionary["Teams"][team][round] = game

def assemble_rounds(num, dictionary):
	sides = dictionary["Sides"]
	n = len(sides["Side A"])
	for j in range(1, n + 1)
		cur_round = "Round " + str(j)
		dictionary["Games"][cur_round] = {}
		dictionary["Rounds"][cur_round] + {}
		for i in range(n):
			game = "Game " + str(i)
			team_1 = sides["Side A"][i]
			team_2 = sides["Side B"][i]
			dictionaries["Rounds"][cur_round][game] = {}
			dictionaries["Rounds"][cur_round][game][team_1] = {}
			dictionaries["Rounds"][cur_round][game][team_1]["Score"] = 0
			dictionaries["Rounds"][cur_round][game][team_1]["Result"] = "N"
			dictionaries["Rounds"][cur_round][game][team_2] = {}
			dictionaries["Rounds"][cur_round][game][team_2]["Score"] = 0
			dictionaries["Rounds"][cur_round][game][team_2]["Result"] = "N"
			add_game(dictionary, team_1, cur_round, game)
			add_game(dictionary, team_2, cur_round, game)
		switch_games(dictionary)
	return dictionary

def round_robin(name, players_list):
	n = len(players_list)
	if n < 2: 
		return 
	if is_list(players_list[0]): 
		players_list = [item[0] for item in sorted(players_list, key=itemgetter(1))]	
	players_list.reverse()
	dictionary = {}
	dictionary["name"] = name
	dictionary["Current Round"] = 0
	dictionary["Games"] = {}
	dictionary["Sides"] = {}
	dictionary["Sides"]["Side A"] = []
	dictionary["Sides"]["Side B"] = []
	dictionary["Teams"] = {}
	for i in range(n):
		if i % 2: 
			dictionary["Sides"]["Side A"].append(players_list[i])
		else: 
			dictionary["Sides"]["Side B"].append(players_list[i])
	if len(dictionary["Sides"]["Side A"]) != len(dictionary["Side B"]):
		dictionary["Sides"]["Side B"].append("Bye")
	return dictionary

def determine_result(dictionary, round, a, b, a_to_b_result):
	game = dictionary["Teams"][a][round]
	if game == dictionary["Teams"][b][round]: 
		dictionary["Rounds"][round][game][a]["Result"] = a_to_b_result
		dictionary["Rounds"][round][game][b]["Result"] = helpers.opposite(a_to_b_result)
		


if __name__ == '__main__':
	# d0 = round_robin([["chicken", 3], ["duck", 1], ["squirrel", 40]])
	d1 = round_robin(["chicken", "duck"])
	round_robin_elimination("chicken", "duck", d1)
	d2 = round_robin(["chicken", "duck", "squirrel"])
