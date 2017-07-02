def elo(r1, r2, outcome, K=32):
	"""
	INPUTS 
	------
	r1: first player's ELO Rank
	r2: second player's ELO Rank
	outcome: enum (W, L, T) for Win, Lose, Tie
	K: a hyperparameter 

	OUTPUTS
	-------
	return (r1_prime, r2_prime)

	the outcome is 'W' if r1 beats r2 and 'L' if r1 loses to r2
	"""
	R1 = 10**(float(winner)/float(400))
	R2 = 10**(float(loser)/float(400))
	E1 = float(R1)/float(R1 + R2)
	E2 = float(R2)/float(R1 + R2)
	S1 = 1.0
	if outcome == 'T': 
		S1 = 0.5
	if outcome == 'L':
		S1 = 0
	S2 = 1.0 - S1 
	r1_prime = r1 + K*(S1 - E1)
	r2_prime = r2 + K*(S2 - E2)
	return (r1_prime, r2_prime)

def calculate_elo_scores(results_array):
	'''
	INPUTS
	------
	results_array: a two-dimensional array
		[[username (string): player 1, username (string): player 2, float: score 1, float: score 2, result (string): 'W', float: K (optional)], ...]
		Those 

	OUTPUTS
	-------
	dictionary: key - username, value - ELO
	'''
	dictionary = {}
	for elo_item in results_array: 

		k = None
		if len(elo_item) == 5:
			player_1, player_2, score_1, score_2, match_result = elo_item 
		else: 
			player_1, player_2, score_1, score_2, match_result, k = elo_item 
		
		if player_1 not in dictionary: 
			dictionary[player_1] = 1000
		if player_2 not in dictionary: 
			dictionary[player_2] = 1000

		if k: 
			dictionary[player_1], dictionary[player_2] = elo(score_1, score_2, match_result, k)
		else: 
			dictionary[player_1], dictionary[player_2] = elo(score_1, score_2, match_result)

	return dictionary

