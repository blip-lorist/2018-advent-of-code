import operator
# configurable
# size of grid
# serial number


def find_highest_cell(grid):
    cell_locations_and_score = {}
    grid_wall = len(grid) - 1
    for idx_row, row in enumerate(grid):
        for idx_col, col in enumerate(row):
            if (idx_row + 2 > grid_wall) or (idx_col + 2 > grid_wall):
                continue

            top_left_x = idx_col
            top_left_y = idx_row
            cell_score = 0
            for y in range(top_left_y, top_left_y + 3):
                for x in range(top_left_x, top_left_x + 3):
                    cell_score += grid[y][x]

            cell_key = (top_left_x, top_left_y)
            cell_locations_and_score[cell_key] = cell_score

    highest_score_coords = sorted(cell_locations_and_score.items(), key=operator.itemgetter(1))[-1][0]
    print(highest_score_coords[0] + 1)
    print(highest_score_coords[1] + 1)




def generate_fuel_cell_grid(size_of_grid, serial_number):
    grid = []
    for idx_y, y in enumerate(range(1, size_of_grid + 1)):
        row = []
        for idx_x, x in enumerate(range(1, size_of_grid + 1)):
            #if (x > 32 and x < 36) and (y > 44 and y < 48):
            power_level = get_power_level(x, y, serial_number)
            row.append(power_level)

        #if len(row) != 0:
        grid.append(row)

    return grid


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

grid = generate_fuel_cell_grid(300, 7857)
find_highest_cell(grid)
