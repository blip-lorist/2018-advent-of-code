from collections import Counter
from operator import add

with open("input.txt","r") as f:
    points_and_velocities = f.readlines()

points_and_velocities = [x.strip() for x in points_and_velocities]

seconds = 0
start_points = []
velocities = []

for point_and_velocity in points_and_velocities:
        point_and_velocity=  point_and_velocity.split("=")
        point = point_and_velocity[1].replace("<","").replace("> velocity","")
        point = point.split(",")
        point = [int(x) for x in point]

        velocity = point_and_velocity[2].replace("<","").replace(">","")
        velocity = velocity.split(",")
        velocity = [int(x) for x in velocity]

        start_points.append(point)
        point_x = point[0]
        point_y = point[1]

        velocities.append(velocity)

while True:
    min_x = None
    min_y = None

    max_x = None
    max_y = None


    ascii_stats = Counter()
    # Get drawing bounds
    for point in start_points:
        point_x = point[0]
        point_y = point[1]

        ascii_stats[point_x] += 1

        if min_x is None or point_x < min_x:
            min_x = point_x

        if min_y is None or point_y < min_y:
            min_y = point_y

        if max_x is None or point_x > max_x:
            max_x = point_x

        if max_y is None or point_y > max_y:
            max_y = point_y

    # Crude heuristic #1: if 20% of the points have a matching x value, then likely text
    #if float(sorted(ascii_stats.values())[-1])/len(start_points) > 0.20:

    # Crude heuristic #2: If the larger ASCII has more than 20 shared x values, then likely text
    # It worked!
    if float(sorted(ascii_stats.values())[-1]) > 20:
        # likely to be text
        # Draw the points
        for y in range(min_y, max_y+1):
            line = []
            for x in range(min_x, max_x+1):
                if [x,y] in start_points:
                    line.append("#")
                else:
                    line.append(" ")
            print("".join(line))
        print("")


    # transform based on velocity
    new_points = []
    for idx, start_point in enumerate(start_points):
        transform = velocities[idx]
        new_point = list(map(add, start_point, transform))
        new_points.append(new_point)

    start_points = new_points

    # inc seconds
    seconds += 1



