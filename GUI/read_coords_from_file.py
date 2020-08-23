"""
Format : 
x0 y0
x1 y1
.....
xN yN

"""

vertices = []
file = open("file.txt", "r")
for line in file:
    coords = line[:-1].split(" ")
    vertices.append((int(coords[0]), int(coords[1])))
print(vertices)
