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
def add_game_to_team(dictionary, team, game):
	if team not in dictionary["Teams"]:
		dictionary["Teams"][team] = []
	dictionary["Teams"][team].append(game)
	return dictionary

def round_robin(name, players_list, groups):
	n = len(players_list)
	dictionary = {}
	dictionary["Pools"] = {}

	pools = [[] for i in range(groups)]
	for j in range(n):
		pools[j % groups].append(players_list[j])
	for k in range(groups):
		dictionary["Pools"]["Pool " + str(k + 1)] = round_robin_helper("Pool " + str(k + 1), pools[k])
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
	dictionary["Games"] = {}
	dictionary["Sides"] = {}
	dictionary["Teams"] = {}
	counter = 1
	for i in range(n):
		for j in range(i + 1, n):
			team_1 = players_list[i]
			team_2 = players_list[j]
			dictionary["Games"][counter] = helpers.make_empty_game(team_1, team_2)
			add_game_to_team(dictionary, team_1, counter)
			add_game_to_team(dictionary, team_2, counter)
			counter += 1
	return dictionary


def all_games_complete(dictionary):
	for game in dictionary["Games"]:
		if helpers.is_game_complete(dictionary["Games"][game]) == False:
			return False
	return True

def get_team_ranks(dictionary):
	dictionary["Records"] = {}
	dictionary["Rankings"] = []
	for team in dictionary["Teams"]: 
		dictionary["Records"][team] = {"W": 0, "L": 0, "T": 0}
		for game in dictionary["Teams"][team]:
			outcome = dictionary["Rounds"][game][team]['Result']
			dictionary["Records"][team][outcome] += 1
		if "Bye" in dictionary["Records"]["Team"]: 
			dictionary["Records"][team]["W"] -= 1
	team_prop_win_pairs = [(team, float(dictionary["Records"][team]['W']/dictionary["Records"][team]['L'])) for team in dictionary["Teams"]]
	dictionary["Ranking"] = [item[0] for item in sorted(team_prop_win_pais, key=lambda x: x[1])]
	return dictionary

def set_result(dictionary, pool, a, b, score_a, score_b, a_to_b_result):
	seed_dictionary = dictionary["Pools"][pool]
	
	possible_game = list(set(seed_dictionary["Teams"][a]) & set(seed_dictionary["Teams"][b]))
	print possible_game
	if len(possible_game) > 0:
		game = possible_game[0] 
		# print seed_dictionary["Games"][game]
		seed_dictionary["Games"][game][a]["Result"] = a_to_b_result
		seed_dictionary["Games"][game][a]["Score"] = score_a
		seed_dictionary["Games"][game][b]["Result"] = helpers.opposite(a_to_b_result)
		seed_dictionary["Games"][game][b]["Score"] = score_b
		if all_games_complete(seed_dictionary): 
			get_team_rankings(seed_dictionary)
	return dictionary

if __name__ == '__main__':
	d0 = round_robin("Revenge of the Chickens", ["chicken", "duck", "squirrel"], 1)
	set_result(d0, "Pool 1", "squirrel", "duck", 10, 5, 'W')
	set_result(d0, "Pool 1", "chicken", "duck", 2, 1, 'L')
	print d0
