from math import sqrt
from random import randint


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


NUMBER_VERTICES = 10
WIDTH = HEIGHT = 100  # dimension of the canvas

vertices = []
visited_vertices = [0]  # by default, the graph starts with the first vertex
path = [0]
current_vertex = 0

print("* Nearest Neighbour Algorithm *")
print("Number of vertices :", NUMBER_VERTICES, "| Dimensions of the canvas : (" + str(WIDTH), ";", str(HEIGHT) + ")\n")
print("Vertices coordinates :")
for i in range(NUMBER_VERTICES):
    vertices.append(Vertex(randint(0, WIDTH), randint(0, HEIGHT)))
    print(i, ": (" + str(vertices[i].x), ";", str(vertices[i].y) + ")")

while len(visited_vertices) < len(vertices):
    global nearest_vertex
    record_distance = dist(0, 0, WIDTH, HEIGHT)
    for i in range(len(vertices)):
        if i not in visited_vertices:
            d = dist(vertices[i].x, vertices[i].y, vertices[current_vertex].x, vertices[current_vertex].y)
            if d < record_distance:
                nearest_vertex = i
                record_distance = d
    visited_vertices.append(nearest_vertex)
    path.append(nearest_vertex)
    current_vertex = nearest_vertex

print("Path :", path)
print("Adjacency matrix :")
adjacency_matrix = [[0 for col in range(NUMBER_VERTICES)] for row in range(NUMBER_VERTICES)]
for i in range(NUMBER_VERTICES - 1):
    adjacency_matrix[path[i]][path[i + 1]] = 1
    adjacency_matrix[path[i + 1]][path[i]] = 1
for row in adjacency_matrix:
    print(*row)
    
