import matplotlib.pyplot as plt
import networkx as nx
from math import sqrt
from random import randint


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


NUMBER_VERTICES = 15
WIDTH = HEIGHT = 100  # dimension of the canvas
VERTEX_SIZE = 150

vertices = []
G = nx.Graph()

# variables for the initialisation path
visited_vertices = [0]  # by default, the graph starts with the first vertex
path1 = [0]
current_vertex = 0
adjacency_matrix1 = [[0 for col in range(NUMBER_VERTICES)] for row in range(NUMBER_VERTICES)]

print("* 2-opt Algorithm *")
print("Number of vertices :", NUMBER_VERTICES, "| Dimensions of the canvas : (" + str(WIDTH), ";", str(HEIGHT) + ")\n")
print("Vertices coordinates :")
for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(randint(0, WIDTH), randint(0, HEIGHT))
    vertices.append(new_vertex)
    G.add_node(i, pos=(new_vertex.x, new_vertex.y))
    print(i, ": (" + str(vertices[i].x), ";", str(vertices[i].y) + ")")

# initialisation graph using the nearest neighbour algorithm
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
    path1.append(nearest_vertex)
    current_vertex = nearest_vertex

print("---------------------------------------------")
print("* Initialisation Graph Using Nn Algorithm *")
print("Path :", path1)
print("Adjacency matrix :")
for i in range(NUMBER_VERTICES - 1):
    adjacency_matrix1[path1[i]][path1[i + 1]] = 1
    adjacency_matrix1[path1[i + 1]][path1[i]] = 1
for row in adjacency_matrix1:
    print(*row)

print("---------------------------------------------")


def intersection(p1, p2, q1, q2):
    det = (p2.x - p1.x) * (q2.y - q1.y) - (q2.x - q1.x) * (p2.y - p1.y)
    if det == 0:
        return False
    else:
        lamb = ((q2.y - q1.y) * (q2.x - p1.x) + (q1.x - q2.x) * (q2.y - p1.y)) / det
        gamma = ((p1.y - p2.y) * (q2.x - p1.x) + (p2.x - p1.x) * (q2.y - p1.y)) / det
        return (0 < lamb < 1) and (0 < gamma < 1)


# variables for the solving algorithm
adjacency_matrix2 = [[0 for col in range(NUMBER_VERTICES)] for row in range(NUMBER_VERTICES)]

print("* Solving Algorithm *")
number_intersections = 1  # suppose there is initially at least one intersection
while number_intersections > 0:
    number_intersections = 0
    for i in range(len(vertices) - 2):
        for j in range(i + 2, len(vertices) - 1):
            if i != j and (i + 1) != j:
                inter = intersection(vertices[i], vertices[i + 1], vertices[j], vertices[j + 1])
                if inter:
                    vertices[i + 1], vertices[j] = vertices[j], vertices[i + 1]  # swap the two vertices
                    path1[i + 1], path1[j] = path1[j], path1[i + 1]
                    number_intersections += 1

print("Path :", path1)
for i in range(NUMBER_VERTICES - 1):
    G.add_edge(path1[i], path1[i + 1])

pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, node_size=VERTEX_SIZE, node_color='orange', with_labels=True)
plt.show()
