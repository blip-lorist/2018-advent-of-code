from llist import dllist
def play_marbles(num_players, max_score):

    circle = dllist()
    scorecard = {}
    highest_score = 0
    marble_value = 0
    current_marble_idx = 0

    #while highest_score < max_score:
    while marble_value < 26:
        for player in range(1, num_players + 1):
            # place marble
            current_marble_idx = place_marble(circle, marble_value, current_marble_idx)

            #score = calculate_points(player, marble_value)

            # track max score
            #if score > max_score:
            #    max_score = score

            # add points to scorecard
            #if player in scorecard.keys():
            #    scorecard[player] += score
            #else:
            #    scorecard[player] = score

            marble_value += 1
            print(circle)


def place_marble(circle, marble_value, current_marble_idx):
    total_marble_count = circle.size
    if total_marble_count == 0:
        last_marble_idx = None
    else:
        last_marble_idx = total_marble_count - 1

    if total_marble_count  == 0 or total_marble_count == 1:
        # When the circle contains none or one marble
        circle.append(marble_value)
        current_marble_idx = circle.size - 1
        return current_marble_idx

    if marble_value % 23 == 0:
        remove_marble_idx = current_marble_idx - 7
        marble_to_remove = circle.nodeat(remove_marble_idx)
        circle.remove(marble_to_remove)
        current_marble_idx = remove_marble_idx
        return current_marble_idx

    if current_marble_idx == last_marble_idx:
        # loop to the start of the circle
        second_place_marble = circle.nodeat(1)
        circle.insert(marble_value, second_place_marble)
        current_marble_idx = 1
        return current_marble_idx

    if current_marble_idx == (last_marble_idx - 1):
        # place at end of circle
        circle.append(marble_value)
        current_marble_idx = circle.size - 1
        return current_marble_idx


    # Otherwise place at center of circle
    second_place_idx = current_marble_idx + 2
    second_place_marble = circle.nodeat(second_place_idx)
    circle.insert(marble_value, second_place_marble)
    current_marble_idx = second_place_idx

    return current_marble_idx

play_marbles(9, 32)







