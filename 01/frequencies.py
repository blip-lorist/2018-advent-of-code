# Read the input
with open("input.txt", "r") as f:
    frequency_changes = f.readlines()

# Remove whitespace
frequency_changes = [x.strip() for x in frequency_changes]

frequency = 0

for frequency_change in frequency_changes:
    if frequency_change[0] == "+":
        frequency += int(frequency_change[1:])
    elif frequency_change[0] == "-":
        frequency -= int(frequency_change[1:])
    else:
        raise ValueError("Operator not supported")


print(frequency)
