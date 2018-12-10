with open("mini_input.txt","r") as f:
    points_and_velocities = f.readlines()

points_and_velocities = [x.strip() for x in points_and_velocities]

start_points = []
min_x = None
min_y = None

max_x = None
max_y = None

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

    if min_x is None or point_x < min_x:
        min_x = point_x

    if min_y is None or point_y < min_y:
        min_y = point_y

    if max_x is None or point_x > max_x:
        max_x = point_x

    if max_y is None or point_y > max_y:
        max_y = point_y



# Draw the points
for y in range(min_y, max_y+1):
    line = []
    for x in range(min_x, max_x+1):
        if [x,y] in start_points:
            line.append("#")
        else:
            line.append(".")
    print("".join(line))



