import os
import binascii

def opposite(word):
	if word == 'W':
		return 'L'
	if word == 'L':
		return 'W'
	else: 
		return word


def make_empty_game(team_1, team_2):
	dictionary = {}
	dictionary[team_1] = {}
	dictionary[team_1]["Score"] = 0
	dictionary[team_1]["Result"] = "N"
	dictionary[team_2] = {}
	dictionary[team_2]["Score"] = 0
	dictionary[team_2]["Result"] = "N"
	return dictionary

def get_random_hash():
	return binascii.hexlify(os.urandom(16))