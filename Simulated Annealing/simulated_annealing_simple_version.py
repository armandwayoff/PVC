import matplotlib.pyplot as plt
from random import *
from math import *


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(v1, v2):
    return sqrt((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)


def total_distance(lst):
    d = 0
    for j in range(len(lst) - 1):
        d += dist(lst[j], lst[j + 1])
    return d


def reverse_sublist(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst


NUMBER_VERTICES = 20
NUM_MARKOV_CHAINS = 10 ** 3
LENGTH_MARKOV_CHAINS = 500
ALPHA = .99

temperature = 50
vertices = []
path = []

for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(uniform(0, 10), uniform(0, 10))
    vertices.append(new_vertex)
    path.append(new_vertex)
path.append(vertices[0])

record_distance = total_distance(path)
for _ in range(NUM_MARKOV_CHAINS):
    temperature *= ALPHA
    for _ in range(LENGTH_MARKOV_CHAINS):
        selected_vertices = sample(range(1, NUMBER_VERTICES + 1), 2)
        test = path.copy()
        test = reverse_sublist(test, selected_vertices[0], selected_vertices[1])
        test_distance = total_distance(test)
        if test_distance < record_distance:
            record_distance = test_distance
            path = test
        else:
            r = uniform(0, 1)
            if r < exp((record_distance - test_distance) / temperature):
                record_distance = test_distance

for i in range(len(path) - 1):
    plt.plot([path[i].x, path[i + 1].x], [path[i].y, path[i + 1].y], 'b')
for vertex in vertices:
    plt.plot(vertex.x, vertex.y, 'bo')

plt.show()
