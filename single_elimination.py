import helpers

def single_elimination(name, players_list):
	dictionary = {}
	dictionary["Rounds"] = {}
	dictionary["Games"] = {}
	for player in players_list: 


def insert_into_dictionary(rounds_dictionary, player): 
	max_round = max(rounds_dictionary.keys())
	cur_round_dictionary = rounds_dictionary[1]
	'''
	3 cases: 
	1. no rounds created -> get bye, connect parent to this hash if one exists
	2. a round is there, but bye round -> transform bye round
	3. we've run out of spots -> add new round, add new game, link old layer to hash of new game
	'''
	
def find_first_empty_spot(cur_round_dictionary, max_round):
	expected_games(max_round)
	largest_game_index = max(cur_round_dictionary.keys())
	if "Bye" in cur_round_dictionary[largest_game_index]: 
		return largest_game_index
	else: 
		if largest_game_index < 2**(max_round - 1): 
			return largest_game_index + 1
		else: 
			return -1

def get_next_game(round, game):
	return (round + 1, (game + 1)/2)

def modify_bye_game(bye_dictionary, team_2):
	bye_dictionary.keys().remove("Bye")
	other_team = bye_dictionary.keys()[0]
	bye_dictionary[""]
def get_bye(player):
	dictionary = {}
	dictionary[player] = {}
	dictionary[player]["Score"] = 0
	dictionary[player]["Result"] = "W"
	dictionary["Bye"] = {}
	dictionary["Bye"]["Score"] = 0
	dictionary["Bye"]["Result"] = "L"
	return dictionary

