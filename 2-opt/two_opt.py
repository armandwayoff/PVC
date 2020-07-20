import matplotlib.pyplot as plt
import networkx as nx
from math import sqrt
from random import randint, sample


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def total_distance(lst):
    d = 0
    for j in range(len(lst) - 1):
        d += dist(vertices[lst[j]].x, vertices[lst[j]].y, vertices[lst[j + 1]].x, vertices[lst[j + 1]].y)
    return d


def reverse_sublist(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst


NUMBER_VERTICES = 100
WIDTH = HEIGHT = 100  # dimension of the canvas
NUMBER_ITERATIONS = 10 ** 5
VERTEX_SIZE = 150

vertices = []
path = []
d = []

G = nx.Graph()

for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(randint(0, WIDTH), randint(0, HEIGHT))
    vertices.append(new_vertex)
    G.add_node(i, pos=(new_vertex.x, new_vertex.y))
    path.append(i)

a = []
record_distance = dist(0, 0, WIDTH, HEIGHT) * NUMBER_VERTICES
for i in range(NUMBER_ITERATIONS):
    selected_vertices = sample(range(1, NUMBER_VERTICES), 2)
    test = path.copy()
    test = reverse_sublist(test, selected_vertices[0], selected_vertices[1])
    test_distance = total_distance(test)
    if test_distance < record_distance:
        record_distance = test_distance
        path = test
        a.append(i)
        d.append(record_distance)

for i in range(NUMBER_VERTICES - 1):
    G.add_edge(path[i], path[i + 1])

plt.figure("Distance Totale")
plt.plot(a, d)

plt.figure("Graph")
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, node_size=VERTEX_SIZE, node_color='orange', with_labels=True)

plt.show()
