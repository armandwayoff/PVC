from math import sqrt
from random import randint


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


number_vertices = 20
width = height = 50  # dimension of the canvas

vertices = []
visited_vertices = [0]  # by default, the graph starts with the first vertex
current_vertex = 0
path = [0]

print("Vertices coordinates :")
for i in range(number_vertices):
    vertices.append(Vertex(randint(0, width), randint(0, height)))
    print(i, ": (" + str(vertices[i].x), ";", str(vertices[i].y) + ")")

while len(visited_vertices) < len(vertices):
    global nearest_vertex
    record_distance = max(width, height) ** 2
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
adjacency_matrix = [[0 for col in range(number_vertices)] for row in range(number_vertices)]
for i in range(number_vertices - 1):
    adjacency_matrix[path[i]][path[i + 1]] = 1
    adjacency_matrix[path[i + 1]][path[i]] = 1
for row in adjacency_matrix:
    print(row)
