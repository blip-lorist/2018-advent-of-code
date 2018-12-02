from collections import Counter
with open("input.txt", "r") as f:
    box_ids = f.readlines()

box_ids = [x.strip() for x in box_ids]
box_ids = [list(x) for x in box_ids]

has_similar_letters = []
for idx, box_id in enumerate(box_ids):
    for idx2, box_id2 in enumerate(box_ids):
        if idx == idx2:
            continue

        similar_letters = []
        for letter_idx, letter in enumerate(box_id):
            if box_id2[letter_idx] == letter:
                similar_letters.append(letter)


        if len(similar_letters) == (len(box_id) - 1):
            similar_letters = "".join(similar_letters)
            # Since it's a nested loop, might have
            # the same value twice
            has_similar_letters.append(similar_letters)

print(set(has_similar_letters))

