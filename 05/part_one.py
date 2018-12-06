with open("input.txt", "r") as f:
    polymer = f.readline()
    #polymer = "dabAcCaCBAcCcaDA"

polymer = polymer.strip()
polymer = list(polymer)

has_reactions = True
while has_reactions:
    has_reactions = False
    for idx, unit in enumerate(polymer):
        if idx == (len(polymer) - 1):
            break
        unit2 = polymer[idx + 1]
        if isinstance(unit, str) and isinstance(unit2, str):
            if (unit.lower() == unit2.lower()) and (unit != unit2):
                has_reactions = True
                polymer[idx] = 0
                polymer[idx+1] = 0

    polymer = list(filter(lambda a: a != 0, polymer))

print(len(polymer))

