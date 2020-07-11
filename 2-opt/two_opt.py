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
visited_vertices = [0]  # by default, the graph starts with the first vertex
path = [0]
current_vertex = 0

adjacency_matrix = [[0 for col in range(NUMBER_VERTICES)] for row in range(NUMBER_VERTICES)]

G = nx.Graph()

print("* 2-opt Algorithm *")
print("Number of vertices :", NUMBER_VERTICES, "| Dimensions of the canvas : (" + str(WIDTH), ";", str(HEIGHT) + ")\n")
print("Vertices coordinates :")
for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(randint(0, WIDTH), randint(0, HEIGHT))
    vertices.append(new_vertex)
    G.add_node(i, pos=(new_vertex.x, new_vertex.y))
    print(i, ": (" + str(vertices[i].x), ";", str(vertices[i].y) + ")")

# Intialisation graph using the nearest neighbour algorithm
while len(visited_vertices) < len(vertices):
    global nearest_vertex
    record_distance = dist(0, 0, WIDTH, HEIGHT)
    for i in range(len(vertices)):
        if i not in visited_vertices:
            d = dist(vertices[i].x, vertices[i].y, vertices[current_vertex].x, vertices[current_vertex].y)
            if d < record_distance:
                nearest_vertex = i
                record_distance = d
    G.add_edge(nearest_vertex, current_vertex)
    visited_vertices.append(nearest_vertex)
    path.append(nearest_vertex)
    current_vertex = nearest_vertex

print("* Initailisation Graph using NN Algorithm *")
print("Path :", path)
print("Adjacency matrix :")
for i in range(NUMBER_VERTICES - 1):
    adjacency_matrix[path[i]][path[i + 1]] = 1
    adjacency_matrix[path[i + 1]][path[i]] = 1
for row in adjacency_matrix:
    print(*row)

pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, node_size=VERTEX_SIZE, node_color='orange', with_labels=True)
plt.show()
