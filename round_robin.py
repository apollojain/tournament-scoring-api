from operator import itemgetter

def is_list(item):
	if isinstance(item, list):
		return True
	else: 
		return False

def round_robin(players_list):
	n = len(players_list)
	if n < 2: 
		return 
	if is_list(players_list[0]): 
		players_list = [item[0] for item in sorted(players_list, key=itemgetter(1))]	
	players_list.reverse()
	dictionary = {}
	i = 0
	while i < n - 2: 
		dictionary[players_list[i]] = players_list[i + 2]
		if i < n - 3:
			dictionary[players_list[i + 1]] = players_list[i + 3]
		i += 1
	dictionary[players_list[n - 2]] = players_list[0]
	dictionary[players_list[n - 1]] = players_list[1]
	return dictionary

def round_robin_elimination(winner, loser, dictionary):
	if winner in dictionary and loser in dictionary:
		dictionary[winner] = dictionary[loser]

if __name__ == '__main__':
	# d0 = round_robin([["chicken", 3], ["duck", 1], ["squirrel", 40]])
	d1 = round_robin(["chicken", "duck"])
	round_robin_elimination("chicken", "duck", d1)
	d2 = round_robin(["chicken", "duck", "squirrel"])
