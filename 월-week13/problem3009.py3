points = [] 

for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))

x_coords = []
y_coords = []

for i in points:
    x_coords.append(i[0])
    y_coords.append(i[1])

fourth_x = x_coords[0]
fourth_y = y_coords[0]

if x_coords[1] == x_coords[2]:
    fourth_x = x_coords[0]
elif x_coords[0] == x_coords[2]:
    fourth_x = x_coords[1]
else:
    fourth_x = x_coords[2]

if y_coords[1] == y_coords[2]:
    fourth_y = y_coords[0]
elif y_coords[0] == y_coords[2]:
    fourth_y = y_coords[1]
else:
    fourth_y = y_coords[2]

print(fourth_x, fourth_y)