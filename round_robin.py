from operator import itemgetter
import helpers

def is_list(item):
	if isinstance(item, list):
		return True
	else: 
		return False

def switch_games(dictionary):
	dictionary["Sides"]["Side A"].append(dictionary["Sides"]["Side A"].pop(0))
	return dictionary
def add_game_to_team(dictionary, team, round, game):
	if team not in dictionary["Teams"]:
		dictionary["Teams"][team] = {}
	dictionary["Teams"][team][round] = game
	return dictionary

def assemble_rounds(dictionary):
	sides = dictionary["Sides"]
	n = len(sides["Side A"])
	for j in range(1, n + 1):
		cur_round = "Round " + str(j)
		dictionary["Games"][cur_round] = {}
		dictionary["Rounds"][cur_round] = {}
		for i in range(n):
			game = "Game " + str(i)
			team_1 = sides["Side A"][i]
			team_2 = sides["Side B"][i]
			dictionary["Rounds"][cur_round][game] = helpers.make_empty_game(team_1, team_2)
			add_game_to_team(dictionary, team_1, cur_round, game)
			add_game_to_team(dictionary, team_2, cur_round, game)
		switch_games(dictionary)
	return dictionary

def round_robin(name, players_list, groups):
	n = len(players_list)
	dictionary = {}
	dictionary["Pools"] = {}

	pools = [[] for i in range(groups)]
	for j in range(n):
		pools[j % groups].append(players_list[j])
	for k in range(groups):
		dictionary["Pools"]["Pool " + str(k)] = round_robin_helper("Pool " + str(k), polls[k])
	return dictionary

def round_robin_helper(name, players_list):
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
	dictionary["Rounds"] = {}
	for i in range(n):
		if i % 2: 
			dictionary["Sides"]["Side A"].append(players_list[i])
		else: 
			dictionary["Sides"]["Side B"].append(players_list[i])
	if len(dictionary["Sides"]["Side A"]) != len(dictionary["Sides"]["Side B"]):
		dictionary["Sides"]["Side B"].append("Bye")
	assemble_rounds(dictionary)
	return dictionary

def try_next_round(dictionary):
	cur_round = "Round " + dictionary["Current Round"]
	for game in dictionary["Rounds"][cur_round]: 
		for team in game: 
			if dictionary["Rounds"][cur_round][game][team] == 'N': 
				return dictionary
	switch_games(dictionary)
	dictionary["Current Round"] += 1
	return dictionary

def determine_result(dictionary, round, a, b, score_a, score_b, a_to_b_result):
	game = dictionary["Teams"][a][round]
	if game == dictionary["Teams"][b][round]: 
		dictionary["Rounds"][round][game][a]["Result"] = a_to_b_result
		dictionary["Rounds"][round][game][a]["Score"] = score_a
		dictionary["Rounds"][round][game][b]["Result"] = helpers.opposite(a_to_b_result)
		dictionary["Rounds"][round][game][b]["Score"] = score_b
	try_next_round(dictionary)
	return dictionary

if __name__ == '__main__':
	d0 = round_robin("Revenge of the Chickens", ["chicken", "duck", "squirrel"])
	print d0
