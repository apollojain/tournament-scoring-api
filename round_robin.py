from operator import itemgetter

def is_list(item):
	if isinstance(item, list):
		return True
	else: 
		return False

def assemble_rounds(num, dictionary):
	sides = dictionary["Sides"]
	n = len(sides["Side A"])
	cur_round = "Round " + str(num)
	dictionary["Games"][cur_round] = {}
	dictionary["Rounds"][cur_round] + {}
	for i in range(n):
		game = "Game " + str(i)
		team_1 = sides["Side A"][i]
		team_2 = sides["Side B"][i]
		dictionaries["Rounds"][cur_round][game] = {}
		dictionaries["Rounds"][cur_round][game][team_1] = {}
		dictionaries["Rounds"][cur_round][game][team_2] = {}
def round_robin(name, players_list):
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
	dictionary["Sides"]["Side A"] = []
	dictionary["Sides"]["Side B"] = []
	for i in range(n):
		if i % 2: 
			dictionary["Sides"]["Side A"].append(players_list[i])
		else: 
			dictionary["Sides"]["Side B"].append(players_list[i])
	if len(dictionary["Sides"]["Side A"]) != len(dictionary["Side B"]):
		dictionary["Sides"]["Side B"].append("Bye")
	return dictionary

def round_robin_elimination(winner, loser, dictionary):
	if winner in dictionary and loser in dictionary:
		dictionary[winner] = dictionary[loser]

if __name__ == '__main__':
	# d0 = round_robin([["chicken", 3], ["duck", 1], ["squirrel", 40]])
	d1 = round_robin(["chicken", "duck"])
	round_robin_elimination("chicken", "duck", d1)
	d2 = round_robin(["chicken", "duck", "squirrel"])
