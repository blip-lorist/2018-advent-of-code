from operator import itemgetter

class CoordinateGrid:
    def __init__(self, coordinates):
        # Coordinates are a list containing x,y tuples
        self.coordinates = coordinates
        x_sorted_coordinates = sorted(self.coordinates,key=itemgetter(0))
        y_sorted_coordinates = sorted(self.coordinates,key=itemgetter(1))
        self.min_x = x_sorted_coordinates[0][0]
        self.max_x = x_sorted_coordinates[-1][0]
        self.min_y = y_sorted_coordinates[0][1]
        self.max_y = y_sorted_coordinates[-1][1]


    def finite_coordinates(self):
        finite_coordinates = []
        for coordinate in self.coordinates:
            if (self.min_x < coordinate[0] < self.max_x) and (self.min_y < coordinate[1] < self.max_y):
                finite_coordinates.append(coordinate)

        return finite_coordinates

    def closest_coordinates_report(self):
        # for each location within a max_width x max_height grid,
        # sort all locations into a bucket corresponding to a coordinate
        min_x = self.min_x
        max_x = self.max_x
        min_y = self.min_y
        max_y = self.max_y

        locations_to_measure = []
        closest_coord_dict = {}

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                locations_to_measure.append(tuple([x, y]))

        for location in locations_to_measure:
            measures_to_coordinate = {}
            for coordinate in self.coordinates:
                manhattan_distance = abs(location[0] - coordinate[0]) + abs(location[1] - coordinate[1])
                measures_to_coordinate[coordinate] = manhattan_distance

            sorted_distances = sorted(measures_to_coordinate.items(), key=itemgetter(1))
            if len(sorted_distances) > 2 and sorted_distances[0][1] == sorted_distances[1][1]:
                # location is equally far from two or more coords
                continue

            closest_coord = sorted_distances[0][0]
            if closest_coord in closest_coord_dict.keys():
                closest_coord_dict[closest_coord].append(location)
            else:
                closest_coord_dict[closest_coord] = [location]

        return closest_coord_dict


def main():
    input_file = "mini_input.txt"
    #input_file = "input.txt"
    with open(input_file, "r") as f:
        coordinates = f.readlines()

    coordinates = [x.strip() for x in coordinates]
    formatted_coordinates = []
    for coordinate in coordinates:
        string_coords = coordinate.split(",")
        int_coords = [int(x) for x in string_coords]
        formatted_coordinates.append(tuple(int_coords))

    grid = CoordinateGrid(formatted_coordinates)
    closest_coordinate_report = grid.closest_coordinates_report()
    finite_coordinates = grid.finite_coordinates()

    largest_area = 0
    for finite_coordinate in finite_coordinates:
        area = len(closest_coordinate_report[finite_coordinate])
        if area > largest_area:
            largest_area = area

    return largest_area


print(main())
