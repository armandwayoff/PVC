# inspired by https://www.youtube.com/watch?v=NPE3zncXA5s

import matplotlib.pyplot as plt
import networkx as nx
from math import *
from random import *
import time


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
    lst[start:end + 1] = lst[start:end + 1][::-1]
    return lst


NUMBER_VERTICES = 20
WIDTH = HEIGHT = 1  # dimension of the canvas
NUMBER_ITERATIONS = 10 ** 3
NUMBER_ITERATIONS_PER_CHAIN = 500
VERTEX_SIZE = 120

INITIAL_TEMP = 50
ALPHA = 0.99
T = INITIAL_TEMP

vertices = []
path = []

temperatures = []
distances = []

G = nx.Graph()

for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(uniform(0, WIDTH), uniform(0, HEIGHT))
    vertices.append(new_vertex)
    G.add_node(i, pos=(new_vertex.x, new_vertex.y))
    path.append(i)
path.append(0)

start_time = time.time()

record_distance = dist(0, 0, WIDTH, HEIGHT) * NUMBER_VERTICES
for _ in range(NUMBER_ITERATIONS):
    temperatures.append(T)
    T *= ALPHA
    for _ in range(NUMBER_ITERATIONS_PER_CHAIN):
        selected_vertices = sample(range(1, NUMBER_VERTICES), 2)
        test = path.copy()
        test = reverse_sublist(test, selected_vertices[0], selected_vertices[1])
        test_distance = total_distance(test)
        if test_distance < record_distance:
            record_distance = test_distance
            path = test
        else:
            r = uniform(0, 1)
            if r < exp((record_distance - test_distance) / T):
                record_distance = test_distance
    distances.append(record_distance)

print("--- %s seconds ---" % (time.time() - start_time))

for i in range(NUMBER_VERTICES):
    G.add_edge(path[i], path[i + 1])

plt.subplot(212)
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, node_size=VERTEX_SIZE, node_color='blue', edge_color='cyan', width=3)
plt.title("Path")
plt.subplot(221)
plt.plot(range(len(temperatures)), temperatures)
plt.title("Temperature")
plt.subplot(222)
plt.plot(range(len(distances)), distances)
plt.title("Total Length")
plt.show()
