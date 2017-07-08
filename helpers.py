import os
import binascii

def opposite(word):
	if word == 'W':
		return 'L'
	if word == 'L':
		return 'W'
	else: 
		return word

def is_game_complete(game_dictionary):
	for team in game_dictionary: 
		if game_dictionary[team]['Result'] == 'N':
			return False
	return True


def make_empty_game(team_1, team_2):
	dictionary = {}
	dictionary[team_1] = {}
	dictionary[team_1]["Score"] = 0
	dictionary[team_1]["Result"] = "N"
	dictionary[team_2] = {}
	dictionary[team_2]["Score"] = 0
	dictionary[team_2]["Result"] = "N"
	if team_1 == "Bye": 
		dictionary[team_1]["Result"] = "L"
		dictionary[team_2]["Result"] = "W"
	if team_2 == "Bye":
		dictionary[team_1]["Result"] = "W"
		dictionary[team_2]["Result"] = "L"
	return dictionary

def get_random_hash():
	return binascii.hexlify(os.urandom(16))