from ordered_set import OrderedSet

#input_file = "mini_input.txt"
input_file = "input.txt"
with open(input_file, "r") as f:
    steps = f.readlines()

steps = [x.strip() for x in steps]


def meets_requirements(prereqs, tree):
    if prereqs is None:
        return True

    for prereq in prereqs:
        if prereq not in tree:
            return False

    return True

tree = []
available = OrderedSet()
prereq_lookup = {}

# Build prereq dictionary for each step
for step in steps:
    step = step.split(" ")
    prereq_step = step[1]
    next_step = step[7]

    if next_step in prereq_lookup.keys():
        prereq_lookup[next_step].add(prereq_step)
    else:
        prereq_lookup[next_step] = set(prereq_step)


for step in steps:
    step = step.split(" ")
    prereq_step = step[1]
    next_step = step[7]
    import pdb; pdb.set_trace()

    # start the tree
    if len(tree) == 0:
        prereq = prereq_lookup.get(prereq_step, None)
        if meets_requirements(prereq, tree):
            tree.append(prereq_step)
            available.append(next_step)
            continue


    if prereq_step not in tree:
        available.append(prereq_step)

    if next_step not in tree:
        available.append(next_step)

    available = OrderedSet(sorted(available))
    available_added = False
    for available_step in available:
        prereq = prereq_lookup.get(available_step, None)
        if meets_requirements(prereq, tree) and available_step not in tree:
            tree.append(available_step)
            import pdb; pdb.set_trace()
            available.discard(available_step)
            available_added = True
            break

    if available_added:
        continue

    if len(tree) == (len(prereq_lookup) + 1): # the tree is complete
        continue
    else:
        # no action can be taken this turn
        continue


print("".join(tree))


    # if bst is  empty, insert prereq, put next_step in holding
    # if prereq is not in holding, disregard
    #   # check next_step against holding, sort alphabetically, add to tree


