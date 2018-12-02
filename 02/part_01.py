from collections import Counter

with open("input.txt", "r") as f:
    box_ids = f.readlines()

box_ids = [x.strip() for x in box_ids]
two_id_count = 0
three_id_count = 0

for box_id in box_ids:
    letters = sorted(box_id)
    letter_counter = Counter()
    has_two = False
    has_three = False
    for letter in letters:
        letter_counter[letter] += 1

    for letter, count in letter_counter.items():
        if count == 2:
            has_two = True
        elif count == 3:
            has_three = True

    if has_two:
        two_id_count += 1

    if has_three:
        three_id_count += 1

checksum = two_id_count * three_id_count
print(checksum)

