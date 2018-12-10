import operator
from llist import dllist

def play_marbles(num_players, max_marble_value):

    circle = dllist()
    circle.append(0)
    scorecard = {}
    highest_score = 0
    marble_value = 1
    current_marble_idx = 0

    while marble_value <= max_marble_value:
    #while True:
        for player in range(1, num_players + 1):
            # place marble
            current_marble_idx = place_marble(circle, marble_value, current_marble_idx, player, scorecard)


            marble_value += 1
            #if marble_value == max_marble_value:
            #    break

            if len(scorecard) == 0:
                highest_score = 0
            else:
                highest_score =  max(scorecard.items(), key=operator.itemgetter(1))[1]


    highest_score =  max(scorecard.items(), key=operator.itemgetter(1))[1]
    print(highest_score)


def place_marble(circle, marble_value, current_marble_idx, player, scorecard):
    total_marble_count = circle.size
    last_marble_idx = total_marble_count - 1

    if total_marble_count == 1:
        # When the circle contains none or one marble
        circle.append(marble_value)
        current_marble_idx = circle.size - 1
        return current_marble_idx

    if marble_value % 23 == 0:
        remove_marble_idx = current_marble_idx - 7
        marble_to_remove = circle.nodeat(remove_marble_idx)

        score = marble_value + marble_to_remove.value
        circle.remove(marble_to_remove)
        current_marble_idx = remove_marble_idx

        # update scorecard
        if player in scorecard.keys():
            scorecard[player] += score
        else:
            scorecard[player] = score

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

play_marbles(30, 5807)
#play_marbles(458, 71307)







