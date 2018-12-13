with open("mini_input.txt", "r") as f:
    spread_patterns = f.readlines()

spread_patterns = [x.strip() for x in spread_patterns]

spread_pattern_lookup = {}
for spread_pattern in spread_patterns:
    spread_pattern, outcome = spread_pattern.split("=>")
    spread_pattern = spread_pattern.strip()
    outcome = outcome.strip()
    spread_pattern_lookup[spread_pattern] = outcome

initial_state = list(".........#..#.#..##......###...###...........")
for gen in range(1,21):
    next_state = []
    for idx, pot in enumerate(initial_state):
        neighbor_idx = range(idx - 2, idx + 3)
        neighbors = []
        for nidx in neighbor_idx:
            if nidx < 0 or nidx > (len(initial_state) - 1):
                neighbors.append(".")
            else:
                neighbors.append(initial_state[nidx])

        neighbors = "".join(neighbors)
        pot_outcome = spread_pattern_lookup.get(neighbors, ".")
        next_state.append(pot_outcome)

    print("".join(next_state))
    initial_state = next_state









