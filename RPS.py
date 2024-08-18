def player(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
        return 'R'

    opponent_history.append(prev_play)

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}5

    # Detect Quincy's pattern
    quincy_pattern = ["R", "R", "P", "P", "S"]
    if len(opponent_history) > 5 and opponent_history[-5:] == quincy_pattern:
        return ideal_response[quincy_pattern[0]]

    # Counter Mrugesh's strategy
    if len(opponent_history) >= 10:
        last_ten = opponent_history[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)
        return ideal_response[ideal_response[most_frequent]]

    # Counter Kris's strategy
    if len(opponent_history) > 1:
        return ideal_response[ideal_response[prev_play]]

    # Counter Abbey's strategy
    if len(opponent_history) >= 2:
        last_two = "".join(opponent_history[-2:])
        potential_plays = [
            prev_play + "R",
            prev_play + "P",
            prev_play + "S",
        ]
        if last_two in potential_plays:
            prediction = last_two[-1]
            return ideal_response[prediction]

    # If no specific pattern detected, play randomly
    import random
    return random.choice(['R', 'P', 'S'])
