# configurable
# size of grid
# serial number


def fuel_cell_grid(size_of_grid, serial_number):
    for y in range(1, size_of_grid + 1):
        row = []
        for x in range (1, size_of_grid + 1):
            #if (x + 2 > 300) || (y + 2 > 300):
                # skip if 3x3 block does not fit into grid
            #    continue
            if (x > 32 and x < 36) and (y > 44 and y < 48):
                power_level = get_power_level(x, y, serial_number)
                row.append(power_level)

        if len(row) > 0:
            print(row)




def get_power_level(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    if power_level > 100:
        hundreds_in_power_level = int(power_level / 100)
        hundredths_place = hundreds_in_power_level % 10
        power_level = hundredths_place
    else:
        power_level = 0

    power_level -= 5

    return power_level

#print(get_power_level(122,79,57))
#print(get_power_level(217,196,39))
#print(get_power_level(101,153,71))

fuel_cell_grid(48, 18)
