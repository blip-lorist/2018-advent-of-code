import operator
from llist import dllist

def play_marbles(num_players, max_marble_value):

    circle = dllist()
    circle.append(0)
    scorecard = {}
    highest_score = 0
    marble_value = 1

    while marble_value < max_marble_value:
        for player in range(1, num_players + 1):
            # place marble
            place_marble(circle, marble_value, player, scorecard)


            marble_value += 1
            if marble_value == max_marble_value:
                break


    highest_score =  max(scorecard.items(), key=operator.itemgetter(1))[1]
    print(highest_score)


def place_marble(circle, marble_value, player, scorecard):
    total_marble_count = circle.size
    last_marble_idx = total_marble_count - 1

    if marble_value % 23 == 0:
        circle.rotate(7)
        removed_marble_value = circle.pop()
        circle.rotate(-1)
        score = marble_value + removed_marble_value

        # update scorecard
        if player in scorecard.keys():
            scorecard[player] += score
        else:
            scorecard[player] = score

    else:
        circle.rotate(-1)
        circle.append(marble_value)

#play_marbles(9, 32)
#play_marbles(30, 5807)
play_marbles(458, 71307)







