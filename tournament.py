import helpers

def single_elimination(name, players_list):
	dictionary = {}
	dictionary["Rounds"] = {}
	dictionary["Games"] = {}
	for player in players_list: 


def insert_into_dictionary(rounds_dictionary, player): 
	cur_round = max(rounds_dictionary.keys())
	cur_round_dictionary = rounds_dictionary[cur_round]
	if len(cur_round)

def get_bye(player):
	dictionary = {}
	dictionary[player] = {}
	dictionary[player]["Score"] = 0
	dictionary[player]["Result"] = "W"
	dictionary["Bye"] = {}
	dictionary["Bye"]["Score"] = 0
	dictionary["Bye"]["Result"] = "L"
	return dictionary

