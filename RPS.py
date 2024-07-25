def player(prev_play, opponent_history=[]):
  opponent_history.append(prev_play)
  if len(opponent_history) > 2:
    guess = opponent_history[-2]
  else:
    guess = "R"
  return guess