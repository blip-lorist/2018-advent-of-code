import string
with open("input.txt", "r") as f:
    polymer = f.readline()
    #polymer = "dabAcCaCBAcCcaDA"

polymer = polymer.strip()
polymer = list(polymer)
polymer_lengths = {}

letters = list(string.ascii_lowercase)

for letter in letters:
    polymer_copy = polymer
    polymer_copy = list(filter(lambda a: a != letter and a != letter.upper(), polymer))

    has_reactions = True
    while has_reactions:
        has_reactions = False
        for idx, unit in enumerate(polymer_copy):
            if idx == (len(polymer_copy) - 1):
                break
            unit2 = polymer_copy[idx + 1]
            if isinstance(unit, str) and isinstance(unit2, str):
                if (unit.lower() == unit2.lower()) and (unit != unit2):
                    has_reactions = True
                    polymer_copy[idx] = 0
                    polymer_copy[idx+1] = 0

        polymer_copy = list(filter(lambda a: a != 0, polymer_copy))

    polymer_lengths[letter] = len(polymer_copy)

sorted_polymer_lengths = sorted(polymer_lengths.items(), key=lambda kv: kv[1])
shortest = sorted_polymer_lengths[0]
print(shortest)

