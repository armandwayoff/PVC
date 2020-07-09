import matplotlib.pyplot as plt
import networkx as nx
from math import sqrt
from random import randint
from itertools import permutations


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def totalDist(lst):
    d = 0
    for j in range(len(lst) - 1):
        d += dist(vertices[lst[j]].x, vertices[lst[j]].y, vertices[lst[j + 1]].x, vertices[lst[j + 1]].y)
    return d


NUMBER_VERTICES = 6
WIDTH = HEIGHT = 100  # dimension of the canvas
VERTEX_SIZE = 150

vertices = []

G = nx.Graph()

print("* Brute Force Algorithm *")
print("Number of vertices :", NUMBER_VERTICES, "| Dimensions of the canvas : (" + str(WIDTH), ";", str(HEIGHT) + ")\n")
print("Vertices coordinates :")
for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(randint(0, WIDTH), randint(0, HEIGHT))
    vertices.append(new_vertex)
    G.add_node(i, pos=(new_vertex.x, new_vertex.y))
    print(i, ": (" + str(vertices[i].x), ";", str(vertices[i].y) + ")")

orders = permutations(range(NUMBER_VERTICES))
record_distance = dist(0, 0, WIDTH, HEIGHT) * NUMBER_VERTICES
global record_path
for o in list(orders):
    if totalDist(o) < record_distance:
        record_distance = totalDist(o)
        record_path = o

for v in range(len(record_path) - 1):
    G.add_edge(record_path[v], record_path[v + 1])

print("Shortest Path :", record_path)

pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, node_size=VERTEX_SIZE, node_color='orange', with_labels=True)
plt.show()
